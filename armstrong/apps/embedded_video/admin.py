from django.contrib import admin
from reversion.admin import VersionAdmin

from . import models


class EmbeddedVideoAdmin(VersionAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'summary', 'video', 'sites', ),
        }),

        # TODO: Refactor this into a fieldset_for(some_model) method so it can
        #       be reused in other apps.
        ('Author Information', {
            'fields': ('authors', 'authors_override', 'authors_extra'),
        }),
    )


admin.site.register(models.EmbeddedVideo, EmbeddedVideoAdmin)
