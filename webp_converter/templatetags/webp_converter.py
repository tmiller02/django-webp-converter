from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.cache import cache
from webp_converter.utils import make_image_key
from webp_converter.models import WebPImage

register = template.Library()


@register.simple_tag(takes_context=True)
def static_webp(context, static_path, quality=None):
    try:
        webp_compatible = context['webp_compatible']
    except KeyError:
        raise Exception("'webp_converter.context_processors.webp_support' "
                        "needs to be added to your context processors.")
    if not webp_compatible:
        return static(static_path)
    key = make_image_key(static_path, quality)
    webp_image_url = cache.get(key)
    if not webp_image_url:
        webp_image, _ = WebPImage.objects.get_or_create(
            static_path=static_path, quality=quality)
        webp_image.save_image()
        webp_image_url = webp_image.url
        cache.set(key, webp_image_url)
    return webp_image_url
