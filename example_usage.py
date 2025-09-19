# =============================================================================
# FILE: example_usage.py
# Examples of how to use the web scraper
# =============================================================================

from scraper import WebScraper

def example_basic_usage():
    """Example of basic scraper usage."""
    print("=== EXAMPLE 1: Basic Usage ===")

    scraper = WebScraper(delay=1.0)

    urls = ["https://x.com"]
    #urls = ["https://example.com", "https://httpbin.org/html"]
    search_terms = ["hamas", "qatar"]

    results = scraper.scrape_urls(urls, search_terms)
    scraper.print_results(results)

def example_title_only_search():
    """Example of searching only in page titles."""
    print("\n=== EXAMPLE 2: Title-Only Search ===")

    scraper = WebScraper(delay=1.0)

    urls = ["https://python.org", "https://github.com"]
    search_terms = ["python", "github"]

    results = scraper.scrape_urls(
        urls=urls,
        search_terms=search_terms,
        search_in='title'
    )
    scraper.print_results(results)

def example_case_sensitive():
    """Example of case-sensitive search."""
    print("\n=== EXAMPLE 3: Case-Sensitive Search ===")

    scraper = WebScraper(delay=1.0)

    urls = ["https://python.org"]
    search_terms = ["Python", "PYTHON"]  # Different cases

    results = scraper.scrape_urls(
        urls=urls,
        search_terms=search_terms,
        case_sensitive=True
    )
    scraper.print_results(results)

def example_custom_search():
    """Example with custom URLs and terms."""
    print("\n=== EXAMPLE 4: Custom Search ===")

    # You can customize these for your specific needs
    custom_urls = [
        "https://news.ycombinator.com",
        "https://stackoverflow.com/questions/tagged/python"
    ]

    custom_terms = ["javascript", "python", "react"]

    scraper = WebScraper(delay=2.0)  # Longer delay for politeness

    results = scraper.scrape_urls(
        urls=custom_urls,
        search_terms=custom_terms,
        case_sensitive=False,
        search_in='all'
    )

    scraper.print_results(results)

if __name__ == "__main__":
    # Run all examples
    example_basic_usage()
    example_title_only_search()
    example_case_sensitive()
    example_custom_search()
