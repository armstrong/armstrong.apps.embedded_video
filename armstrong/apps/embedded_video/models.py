from armstrong.core.arm_content.mixins import AuthorsMixin
from armstrong.core.arm_content.mixins import EmbeddedVideoMixin
from armstrong.core.arm_content.fields import EmbeddedVideoField
# TODO: update to new locatoin
from armstrong.core.arm_content.publication.models import PublicationMixin

from django.db import models

from . import settings


class EmbeddedVideoBase(AuthorsMixin, EmbeddedVideoMixin, PublicationMixin,
        models.Model):
    title = models.CharField(max_length=255)
    aspect_ratio = models.CharField(max_length=5,
            choices=settings.ASPECT_RATIOS,
            default=settings.DEFAULT_ASPECT_RATIO)

    # TODO: screen cap thumbnail
    screencap_url = models.URLField()

    class Meta:
        abstract = True


class EmbeddedVideo(EmbeddedVideoBase):
    pass
