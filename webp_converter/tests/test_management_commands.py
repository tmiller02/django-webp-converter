from django.test import TestCase
from django.core.cache import cache
from django.core.management import call_command
from webp_converter.models import WebPImage
from webp_converter.utils import make_image_key


class TestManagementCommands(TestCase):

    def test_clear_cache(self):
        static_path = 'django-test-image.png'
        quality = 80
        key = make_image_key(static_path, quality)
        cache.set(key, 'test')
        assert cache.get(key) == 'test'
        WebPImage.objects.create(
            static_path=static_path, quality=quality)
        assert WebPImage.objects.all().count() == 1
        call_command('clear_webp_cache')
        assert cache.get(key) is None
        assert WebPImage.objects.all().count() == 0

