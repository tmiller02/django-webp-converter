import os
import shutil

from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache
from django.core.files.storage import default_storage

from webp_converter.utils import make_image_key
from webp_converter.models import WebPImage
from webp_converter.conf.settings import WEBP_CONVERTER_PREFIX


class Command(BaseCommand):
    help = "Clear webp cached images"

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--noinput', '--no-input', action='store_false', dest='interactive',
            help="Do NOT prompt the user for input of any kind.",
        )

    def handle(self, *args, **options):

        webp_path = default_storage.path(WEBP_CONVERTER_PREFIX)

        if options['interactive']:
            confirm_message = (
                'This will delete all files in {webp_path}\n\n'
                'Are you sure you want to do this?\n\n'
                "Type 'yes' to continue, or 'no' to cancel: "
            ).format(webp_path=webp_path)
            if input(confirm_message) != 'yes':
                raise CommandError("Clearing webp cache cancelled.")
        self.stdout.write("Deleting cache entries...")
        for webp_image in WebPImage.objects.all().iterator():
            key = make_image_key(webp_image.static_path, webp_image.quality)
            cache.delete(key)
        self.stdout.write("Deleting WebPImage models...")
        WebPImage.objects.all().delete()
        self.stdout.write("Deleting images...")
        if os.path.exists(webp_path):
            shutil.rmtree(webp_path)
        self.stdout.write("Successfully cleared cache")

        if os.path.exists(webp_path):
            shutil.rmtree(webp_path)
