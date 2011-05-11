from armstrong.apps.content.models import Content
from armstrong.core.arm_content.mixins import AuthorsMixin
from armstrong.core.arm_content.mixins import EmbeddedVideoMixin
from armstrong.core.arm_content.fields import EmbeddedVideoField

from django.db import models

from . import settings


class EmbeddedVideoBase(Content, EmbeddedVideoMixin, models.Model):
    aspect_ratio = models.CharField(max_length=5,
            choices=settings.ASPECT_RATIOS,
            default=settings.DEFAULT_ASPECT_RATIO)

    # TODO: screen cap thumbnail
    screencap_url = models.URLField()

    class Meta:
        abstract = True


class EmbeddedVideo(EmbeddedVideoBase):
    pass
