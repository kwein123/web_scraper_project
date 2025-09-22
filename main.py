# =============================================================================
# FILE: main.py
# Main execution script
# =============================================================================

from web_scraper_project.scraper import WebScraper
from web_scraper_project.config import URLS, SEARCH_TERMS, SCRAPER_DELAY, CASE_SENSITIVE, SEARCH_IN

def main():
    """Main function to run the web scraper."""
    print("🔍 Web Scraper Starting...")
    print(f"📝 URLs to scrape: {len(URLS)}")
    print(f"🔎 Search terms: {SEARCH_TERMS}")
    print(f"⏱️  Delay between requests: {SCRAPER_DELAY}s")
    print(f"🔤 Case sensitive: {CASE_SENSITIVE}")
    print(f"📍 Search in: {SEARCH_IN}")
    print("-" * 50)

    # Initialize the scraper
    scraper = WebScraper(delay=SCRAPER_DELAY)

    # Scrape and search
    results = scraper.scrape_urls(
        urls=URLS,
        search_terms=SEARCH_TERMS,
        case_sensitive=CASE_SENSITIVE,
        search_in=SEARCH_IN
    )

    # Print results
    scraper.print_results(results)

    # Optional: Save results to file
    save_results_to_file(results)

def save_results_to_file(results):
    """Save results to a text file."""
    import json
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scraper_results_{timestamp}.json"

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Results saved to: {filename}")
    except Exception as e:
        print(f"\n❌ Error saving results: {e}")

if __name__ == "__main__":
    main()


# =============================================================================
# FILE: test_scraper.py
# Unit tests for the web scraper
# =============================================================================

import unittest
from web_scraper_project.scraper import WebScraper
from bs4 import BeautifulSoup

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.scraper = WebScraper(delay=0.1)  # Short delay for testing

    def test_search_terms_in_text(self):
        """Test the search functionality."""
        text = "This is a test text about Python programming and web development."
        search_terms = ["python", "web", "nonexistent"]

        results = self.scraper.search_terms_in_text(text, search_terms, case_sensitive=False)

        self.assertIn("python", results)
        self.assertIn("web", results)
        self.assertNotIn("nonexistent", results)
        self.assertEqual(len(results["python"]), 1)
        self.assertEqual(len(results["web"]), 1)

    def test_case_sensitive_search(self):
        """Test case sensitive search."""
        text = "Python is different from python"
        search_terms = ["Python"]

        # Case sensitive
        results_sensitive = self.scraper.search_terms_in_text(text, search_terms, case_sensitive=True)
        self.assertEqual(len(results_sensitive["Python"]), 1)

        # Case insensitive
        results_insensitive = self.scraper.search_terms_in_text(text, search_terms, case_sensitive=False)
        self.assertEqual(len(results_insensitive["Python"]), 2)

    def test_fetch_page_invalid_url(self):
        """Test handling of invalid URLs."""
        result = self.scraper.fetch_page("https://this-url-definitely-does-not-exist-12345.com")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
