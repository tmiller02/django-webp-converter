from django.test import TestCase
from django.http import HttpRequest
from webp_converter.context_processors import webp_support

USER_AGENTS = [
    # [0] Chrome - supported browser + supported version
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',

    # [1] Firefox - supported browser + unsupported version
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',

    # [2] Safari - unsupported browser
    'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'
]

class TestContextProcessors(TestCase):

    def setUp(self):
        self.request = HttpRequest()

    def test_no_user_agent(self):
        result = webp_support(self.request)
        webp_supported = result.get('webp_compatible')
        self.assertFalse(webp_supported)

    def test_user_agent_supported_browser_supported_version(self):
        self.request.META['HTTP_USER_AGENT'] = USER_AGENTS[0]
        result = webp_support(self.request)
        webp_supported = result.get('webp_compatible')
        self.assertTrue(webp_supported)

    def test_user_agent_supported_browser_unsupported_version(self):
        self.request.META['HTTP_USER_AGENT'] = USER_AGENTS[1]
        result = webp_support(self.request)
        webp_supported = result.get('webp_compatible')
        self.assertFalse(webp_supported)

    def test_user_agent_unsupported_browser(self):
        self.request.META['HTTP_USER_AGENT'] = USER_AGENTS[2]
        result = webp_support(self.request)
        webp_supported = result.get('webp_compatible')
        self.assertFalse(webp_supported)

    def test_http_accept_header_supported(self):
        self.request.META['HTTP_ACCEPT'] = 'image/webp'
        result = webp_support(self.request)
        webp_supported = result.get('webp_compatible')
        self.assertTrue(webp_supported)

    def test_http_accept_header_unsupported(self):
        self.request.META['HTTP_ACCEPT'] = 'image/png'
        result = webp_support(self.request)
        webp_supported = result.get('webp_compatible')
        self.assertFalse(webp_supported)

    # def test_webp_support_true(self):
    #     request = HttpRequest()
    #     request.META["HTTP_ACCEPT"] = (
    #         "text/html,application/xhtml+xml,application/xml;"
    #         "q=0.9,image/webp,*/*;q=0.8"
    #     )
    #     assert webp_support(request) == {"webp_compatible": True}
    #
    # def test_webp_support_false(self):
    #     request = HttpRequest()
    #     request.META[
    #         "HTTP_ACCEPT"
    #     ] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    #     assert webp_support(request) == {"webp_compatible": False}
