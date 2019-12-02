import os
import hashlib
from PIL import Image

from django.core.files.storage import default_storage
from django.contrib.staticfiles import finders
from django.db import models
from django.utils.encoding import force_bytes

from webp_converter.conf.settings import WEBP_CONVERTER_PREFIX


class WebPImage(models.Model):
    static_path = models.CharField(max_length=512)
    quality = models.PositiveIntegerField()

    class Meta:
        unique_together = (("static_path", "quality"),)

    @property
    def image_absolute_path(self):
        """
        The full image file path found from the static path
        """
        full_image_path = finders.find(self.static_path)
        if not full_image_path:
            raise IOError("Can't find static image.")
        return full_image_path

    @property
    def webp_relative_path(self):
        key = hashlib.md5(force_bytes(self.static_path + str(self.quality))).hexdigest()
        return "{prefix}/{key_1}/{key_2}/{path}.webp".format(
            prefix=WEBP_CONVERTER_PREFIX,
            key_1=key[:2],
            key_2=key[2:8],
            path="".join(self.static_path.split(".")[:-1]),
        )

    @property
    def webp_absolute_path(self):
        """
        The full image file path of the webp image
        """
        return default_storage.path(self.webp_relative_path)

    @property
    def url(self):
        return default_storage.url(self.webp_relative_path)

    def save_image(self):
        image = Image.open(self.image_absolute_path)
        # Create directory structure if it does not exist
        webp_dirname = os.path.dirname(self.webp_absolute_path)
        if not os.path.exists(webp_dirname):
            os.makedirs(webp_dirname)
        image.save(**self._get_save_image_kwargs())

    def _get_save_image_kwargs(self):
        return {
            "format": "WEBP",
            "fp": self.webp_absolute_path,
            "quality": self.quality
        }
