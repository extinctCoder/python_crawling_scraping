# Scrapy settings for product_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "product_scraper"

SPIDER_MODULES = ["product_scraper.spiders"]
NEWSPIDER_MODULE = "product_scraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "product_scraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     "product_scraper.middlewares.ProductScraperSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #    "product_scraper.middlewares.ProductScraperDownloaderMiddleware": 543,
    # "product_scraper.middlewares.ScrapeOpsFakeUserAgentMiddleware": 400,
    "product_scraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware": 400,
    "rotating_proxies.middlewares.RotatingProxyMiddleware": 610,
    "rotating_proxies.middlewares.BanDetectionMiddleware": 620,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     # "product_scraper.pipelines.ProductScraperPipeline": 300,
#     "product_scraper.pipelines.BookPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Scrapeops Config
SCRAPEOPS_API_KEY = "819736af-3870-4b4d-964c-6cd5d92880b7"
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = "https://headers.scrapeops.io/v1/user-agents"
SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = (
    "http://headers.scrapeops.io/v1/browser-headers"
)
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 50
ROTATING_PROXY_LIST = [
    "103.204.208.208:8080",
    "115.127.13.154:8880",
    "103.135.139.121:8080",
    "43.231.22.228:80",
    "103.148.216.125:8080",
    "203.80.189.33:8080",
    "103.250.70.214:8080",
    "103.108.89.164:8082",
    "103.218.25.245:8080",
    "103.239.253.66:8080",
    "103.245.204.214:8080",
    "116.206.61.201:8080",
    "103.221.254.102:48146",
    "27.147.139.154:8090",
    "103.83.232.122:80",
    "103.108.88.41:8080",
    "119.18.149.9:5020",
    "180.211.186.158:8080",
    "119.18.149.34:8080",
    "103.87.212.140:8999",
    "115.127.36.190:222",
    "103.49.114.195:8080",
    "103.60.161.18:8080",
    "103.129.208.242:8080",
    "182.160.100.156:5020",
    "119.18.146.114:5020",
    "103.109.57.250:8889",
    "203.202.245.27:5020",
    "202.40.185.146:8080",
    "202.164.209.69:5020",
    "144.48.111.7:8674",
    "202.5.47.173:5020",
    "103.204.82.34:3212",
    "202.40.185.166:8090",
    "115.127.28.10:8674",
]
