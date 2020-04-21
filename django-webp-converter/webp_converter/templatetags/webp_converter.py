from django import template
from django.templatetags.static import static
from django.core.cache import cache

from webp_converter.utils import make_image_key
from webp_converter.models import WebPImage

register = template.Library()


@register.simple_tag(takes_context=True)
def static_webp(context, static_path, quality=80):
    try:
        webp_compatible = context["webp_compatible"]
    except KeyError:
        raise Exception(
            "'webp_converter.context_processors.webp_support' "
            "needs to be added to your context processors."
        )
    if not webp_compatible:
        return static(static_path)
    key = make_image_key(static_path, quality)
    webp_image_url = cache.get(key)
    if not webp_image_url:
        webp_image, _ = WebPImage.objects.get_or_create(
            static_path=static_path, quality=quality
        )
        if not webp_image.webp_image_exists:
            webp_image.save_webp_image()
        webp_image_url = webp_image.webp_url
        cache.set(key, webp_image_url)
    return webp_image_url
