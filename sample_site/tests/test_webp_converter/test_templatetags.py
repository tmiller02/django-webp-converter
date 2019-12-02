from django.test import TestCase
from django.templatetags.static import static

from webp_converter.templatetags.webp_converter import static_webp
from webp_converter.models import WebPImage


class TestTemplateTags(TestCase):
    def setUp(self):
        self.static_path = "images/django-test-image.png"
        self.webp_image = WebPImage.objects.create(
            static_path=self.static_path, quality=75
        )

    def test_static_webp_templatetag(self):
        context = {"webp_compatible": True}
        result = static_webp(
            context=context, static_path=self.static_path, quality=75)
        assert result == self.webp_image.url

    def test_missing_context(self):
        with self.assertRaises(Exception):
            static_webp(context={}, static_path=self.static_path, quality=75)

    def test_no_webp_support(self):
        context = {"webp_compatible": False}
        result = static_webp(context=context, static_path=self.static_path, quality=75)
        assert result == static(self.webp_image.static_path)
