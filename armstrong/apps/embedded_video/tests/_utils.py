from django.test import TestCase as DjangoTestCase


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
