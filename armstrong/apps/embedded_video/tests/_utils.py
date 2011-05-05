from django.core.management.color import no_style
from django.db import connection
from django.test import TestCase as DjangoTestCase


def create_concrete_table(func):
    style = no_style()
    seen_models = connection.introspection.installed_models(
            connection.introspection.table_names())
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        sql, _references = connection.creation.sql_create_model(self.model,
                style, seen_models)
        cursor = connection.cursor()
        for statement in sql:
            cursor.execute(statement)
    return inner


def destroy_concrete_table(func):
    style = no_style()
    # Assume that there are no references to destroy, these are supposed to be
    # simple models
    references = {}
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        sql = connection.creation.sql_destroy_model(self.model, references,
                style)
        cursor = connection.cursor()
        for statement in sql:
            cursor.execute(statement)
    return inner


# TODO: pull into a common dev package so all armstrong code can use it
def concrete(klass):
    attrs = {'__module__': concrete.__module__, }
    return type("Concrete%s" % klass.__name__, (klass, ), attrs)


class TestCase(DjangoTestCase):
    def assertModelHasField(self, model, field_name, field_class=None):
        self.assertTrue(hasattr(model, field_name))
        field = model._meta.get_field_by_name(field_name)[0]
        if field_class is not None:
            self.assertTrue(isinstance(field, field_class))
