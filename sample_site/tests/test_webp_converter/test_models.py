import os
from django.test import TestCase
from django.contrib.staticfiles import finders
from django.conf import settings
from webp_converter.models import WebPImage
from webp_converter.conf.settings import WEBP_CONVERTER_PREFIX


class TestModels(TestCase):
    def setUp(self):
        self.webp_image = WebPImage(static_path="images/django-test-image.png", quality=80)
        self.invalid_webp_image = WebPImage(static_path="missing.png", quality=80)

    def test_invalid_image_absolute_path(self):
        with self.assertRaisesMessage(Exception, "Can't find static image."):
            return self.invalid_webp_image.image_absolute_path

    def test_valid_image_absolute_path(self):
        assert self.webp_image.image_absolute_path == finders.find(
            "images/django-test-image.png"
        )

    def test_webp_relative_path(self):
        self.assertEqual(
            self.webp_image.webp_relative_path,
            f"{WEBP_CONVERTER_PREFIX}/f2/580a53/images/django-test-image.webp"
        )

    def test_url(self):
        assert (
            self.webp_image.url
            == settings.MEDIA_URL + self.webp_image.webp_relative_path
        )

    def test_save_image_kwargs(self):
        save_image_kwargs = self.webp_image._get_save_image_kwargs()
        assert save_image_kwargs == {
            "format": "WEBP",
            "quality": 80,
            "fp": self.webp_image.webp_absolute_path,
        }

    def test_save_new_image(self):
        assert not os.path.exists(self.webp_image.webp_absolute_path)
        self.webp_image.save_image()
        assert os.path.exists(self.webp_image.webp_absolute_path)
