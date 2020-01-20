import httpagentparser
from setuptools._vendor.packaging import version

webp_supported_browsers = {
    'Chrome': '23.0',
    'Firefox': '65.0',
    'MSEdge': '18.0',
    'Opera': '12.10',
    'Opera Mobile': '12.0'
}

def _check_user_agent(user_agent):
    """ Checks if the USER_AGENT supports webp """

    if user_agent:
        user_agent = httpagentparser.detect(user_agent)
        browser_name = user_agent.get('browser').get('name', '')
        browser_version = user_agent['browser'].get('version', '0')  # version not always provided
    else:  # No USER_AGENT supplied
        return False

    try:
        min_version = webp_supported_browsers[browser_name]
    except KeyError:  # Not a supported browser
        return False
    # Ensure brower version supports WEBP
    if version.parse(browser_version) >= version.parse(min_version):
        return True


def _check_http_accept(http_accept):
    """ Check if HTTP_ACCEPT header includes webp """
    return 'webp' in http_accept


def webp_support(request):
    http_accept = request.META.get('HTTP_ACCEPT', '')
    user_agent = request.META.get('HTTP_USER_AGENT')

    if _check_http_accept(http_accept):
        webp_compatible = True
    elif _check_user_agent(user_agent):
        webp_compatible = True
    else:
        webp_compatible = False

    return {'webp_compatible': webp_compatible}
