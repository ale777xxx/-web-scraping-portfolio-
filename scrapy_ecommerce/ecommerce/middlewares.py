from fake_useragent import UserAgent

class RotateUserAgentMiddleware:
    def __init__(self):
        self.ua = UserAgent()

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', self.ua.random)

class ProxyMiddleware:
    def process_request(self, request, spider):
        proxy = spider.settings.get('HTTP_PROXY') or spider.settings.get('HTTPS_PROXY')
        if proxy:
            request.meta['proxy'] = proxy
