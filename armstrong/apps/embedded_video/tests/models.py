from ._utils import *
from armstrong.core.arm_content.fields import EmbeddedVideoField
import datetime
from django.db.models import ManyToManyField

from .. import models


now = datetime.datetime.now


class EmbeddedVideoBaseTestCase(TestCase):
    @create_concrete_table
    def setUp(self):
        self.model = concrete(models.EmbeddedVideoBase)

    @destroy_concrete_table
    def tearDown(self):
        pass

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

    def test_has_sites_field(self):
        video = self.model.objects.create(title="Random Video", pub_date=now())
        self.assertModelHasField(video, "sites", ManyToManyField)
