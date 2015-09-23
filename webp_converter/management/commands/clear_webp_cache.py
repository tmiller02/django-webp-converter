from django.core.management.base import BaseCommand
from django.core.cache import cache
from webp_converter.utils import delete_webp_folder
from webp_converter.models import WebPImage
from webp_converter.utils import make_image_key, webp_image_querysets


class Command(BaseCommand):
    help = 'Clear webp cached images'

    def handle(self, *args, **options):
        total_count = WebPImage.objects.all().count()
        for qs in webp_image_querysets(total_count):
            for webp_image in qs:
                key = make_image_key(webp_image.static_path, webp_image.quality)
                cache.delete(key)
        WebPImage.objects.all().delete()
        delete_webp_folder()
        self.stdout.write('Successfully cleared cache')
