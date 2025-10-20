BOT_NAME = "ecommerce"

SPIDER_MODULES = ["ecommerce.spiders"]
NEWSPIDER_MODULE = "ecommerce.spiders"

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 8
DOWNLOAD_DELAY = 0.3
RETRY_ENABLED = True
RETRY_TIMES = 3
AUTOTHROTTLE_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    "ecommerce.middlewares.RotateUserAgentMiddleware": 400,
    "ecommerce.middlewares.ProxyMiddleware": 410,
}

ITEM_PIPELINES = {
    "ecommerce.pipelines.CleanProductPipeline": 300,
}

# Optional global proxy (can be set via env and read in settings.py with os.getenv)
# HTTP_PROXY = "http://user:pass@host:port"
# HTTPS_PROXY = "http://user:pass@host:port"
