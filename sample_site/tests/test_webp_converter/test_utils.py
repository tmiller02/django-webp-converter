from django.test import TestCase
from webp_converter import utils
from webp_converter.conf import settings as webp_settings


class TestUtils(TestCase):
    def test_make_image_key(self):
        key = utils.make_image_key("static/path/image.jpg", 60)
        self.assertEqual(
            key,
            webp_settings.WEBP_CONVERTER_CACHE_PREFIX + ":3eac052ec0eaf68475576e75e2305f2b"
        )
