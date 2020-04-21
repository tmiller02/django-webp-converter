from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache
from django.core.files.storage import default_storage

from webp_converter.utils import make_image_key
from webp_converter.models import WebPImage


class Command(BaseCommand):
    help = "Clear webp cached images"

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--noinput', '--no-input', action='store_false', dest='interactive',
            help="Do NOT prompt the user for input of any kind.",
        )

    def handle(self, *args, **options):

        if options['interactive']:
            confirm_message = (
                'This will delete all generated WebP images.\n\n'
                'Are you sure you want to do this?\n\n'
                "Type 'yes' to continue, or 'no' to cancel: "
            )
            if input(confirm_message) != 'yes':
                raise CommandError("Clearing WebP cache cancelled.")
        self.stdout.write("Deleting cache entries, WebP images and WebP models...")
        for webp_image in WebPImage.objects.all().iterator():
            key = make_image_key(webp_image.static_path, webp_image.quality)
            cache.delete(key)
            default_storage.delete(webp_image.webp_relative_path)
            webp_image.delete()
        self.stdout.write("Successfully cleared cache")
