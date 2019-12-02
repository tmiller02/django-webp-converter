from django.conf import settings

WEBP_CONVERTER_PREFIX = getattr(settings, "WEBP_DIRECTORY", "WEBP")
WEBP_CONVERTER_CACHE_PREFIX = getattr(settings, "WEBP_CACHE_PREFIX", "webp_converter")
