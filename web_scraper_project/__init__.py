"""
Web Scraper Project

A simple, respectful web scraper built with Python and BeautifulSoup.
"""

__version__ = "1.0.0"
__author__ = "Kevin Weinrich"
__email__ = "weinrichkevin@gmail.com"

# Import main classes for easy access
from .scraper import WebScraper
from . import config

# Make key components available at package level
__all__ = [
    "WebScraper",
    "config",
    "main",
    "run_scraper",
]

def main():
    """Entry point for the web scraper application."""
    from .cli import main as cli_main
    cli_main()

def run_scraper():
    """Alternative entry point with different name."""
    main()