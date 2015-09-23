import hashlib
import shutil
import os
from django.core.files.storage import default_storage
from django.utils.encoding import force_bytes
from webp_converter.conf.settings import WEBP_CONVERTER_PREFIX
from webp_converter.models import WebPImage


def make_image_key(*args):
    md5_hash = hashlib.md5(force_bytes(':'.join(str(arg) for arg in args)))
    return "webp_converter:%s" % md5_hash.hexdigest()


def webp_image_querysets(total_count, object_number=100):
    for index in range(0, total_count, object_number):
        yield WebPImage.objects.all()[index: index + object_number]


def delete_webp_folder():
    webp_path = default_storage.path(WEBP_CONVERTER_PREFIX)
    if os.path.exists(webp_path):
        shutil.rmtree(webp_path)
