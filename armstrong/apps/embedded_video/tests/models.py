from ._utils import *
from armstrong.core.arm_content.fields import EmbeddedVideoField

from .. import models


class EmbeddedVideoBaseTestCase(TestCase):
    def setUp(self):
        self.model = concrete(models.EmbeddedVideoBase)

    def test_has_title(self):
        video = self.model()
        self.assertModelHasField(video, "title")

    def test_has_a_source_embedded_video_field(self):
        video = self.model()
        self.assertModelHasField(video, "video", EmbeddedVideoField)

    def test_has_a_screencap_url(self):
        video = self.model()
        self.assertModelHasField(video, "screencap_url")

    def test_has_publication_mixin_fields(self):
        video = self.model()
        self.assertModelHasField(video, "pub_date")
        self.assertModelHasField(video, "pub_status")
