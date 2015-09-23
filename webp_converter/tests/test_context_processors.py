from django.test import TestCase
from django.http import HttpRequest
from webp_converter.context_processors import webp_support


class TestContextProcessors(TestCase):

    def test_webp_support_true(self):
        request = HttpRequest()
        request.META['HTTP_ACCEPT'] =\
            'text/html,application/xhtml+xml,application/xml;' \
            'q=0.9,image/webp,*/*;q=0.8'
        assert webp_support(request) == {'webp_compatible': True}

    def test_webp_support_false(self):
        request = HttpRequest()
        request.META['HTTP_ACCEPT'] =\
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        assert webp_support(request) == {'webp_compatible': False}
