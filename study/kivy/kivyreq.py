from kivy.network.urlrequest import UrlRequest


def got_json(req, result):
    for key, value in result['headers'].items():
        print('{}: {}'.format(key, value))

req = UrlRequest('https://httpbin.org/headers', got_json,)
