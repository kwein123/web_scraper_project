# =============================================================================
# FILE: config.py
# Configuration settings for the scraper
# =============================================================================

# URLs to scrape
URLS = [
    #"https://httpbin.org/html",
    #"https://example.com",
    #"https://python.org",
    #"https://docs.python.org/3/",
    #"https://realpython.com"
    "https://nationalreview.com",
	"https://clarionproject.org",
	"https://tranquility.ai"
]

# Terms to search for
SEARCH_TERMS = [
#    "python",
#    "programming",
#    "example",
#    "HTTP",
#    "web",
#    "development"
    "violence",
	"extremism",
	"threats",
	"Charlie",
	"TimePilot",
	"Security"
]

# Scraper settings
SCRAPER_DELAY = 1.0  # Delay between requests in seconds
CASE_SENSITIVE = False
SEARCH_IN = 'all'  # Options: 'all', 'title', 'body', 'links'
