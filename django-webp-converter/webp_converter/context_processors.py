def webp_support(request):
    return {"webp_compatible": "image/webp" in request.META.get("HTTP_ACCEPT", {})}
