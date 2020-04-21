import io
import hashlib
from PIL import Image

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
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
    def webp_url(self):
        return default_storage.url(self.webp_relative_path)

    @property
    def webp_image_exists(self):
        return default_storage.exists(self.webp_relative_path)

    def save_webp_image(self):
        image = Image.open(self.image_absolute_path)
        image_bytes = io.BytesIO()
        image.save(
            fp=image_bytes,
            format="WEBP",
            quality=self.quality
        )
        image_content_file = ContentFile(content=image_bytes.getvalue())
        default_storage.save(self.webp_relative_path, image_content_file)
