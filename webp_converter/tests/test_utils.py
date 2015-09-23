import os
from django.core.files.storage import default_storage
from django.test import TestCase
from webp_converter import utils
from webp_converter.conf import settings as webp_settings
from webp_converter.models import WebPImage


class TestUtils(TestCase):
    def test_make_image_key(self):
        key = utils.make_image_key('static/path/image.jpg', 60)
        assert key == webp_settings.WEBP_CONVERTER_CACHE_PREFIX +\
            ':3eac052ec0eaf68475576e75e2305f2b'

    def test_webp_querysets(self):
        WebPImage.objects.create(static_path='image_1.png', quality=80)
        WebPImage.objects.create(static_path='image_2.png', quality=80)
        WebPImage.objects.create(static_path='image_3.png', quality=80)
        ids = [
            item.id
            for qs in utils.webp_image_querysets(3, 2)
            for item in qs]
        assert ids == [1, 2, 3]

    def test_delete_webp_folder(self):
        webp_image = WebPImage.objects.create(
            static_path='django-test-image.png', quality=60)
        webp_image.save_image()
        webp_path = default_storage.path(webp_settings.WEBP_CONVERTER_PREFIX)
        self.assertTrue(os.path.exists(webp_path))
        utils.delete_webp_folder()
        self.assertFalse(os.path.exists(webp_path))
