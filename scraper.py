# =============================================================================
# FILE: scraper.py
# Main WebScraper class definition
# =============================================================================

import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse
import re
from typing import List, Dict, Set

class WebScraper:
    def __init__(self, delay: float = 1.0):
        """
        Initialize the web scraper.

        Args:
            delay: Delay between requests in seconds (be respectful to servers)
        """
        self.delay = delay
        self.session = requests.Session()
        # Set a user agent to avoid being blocked
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def fetch_page(self, url: str) -> BeautifulSoup:
        """
        Fetch and parse a web page.

        Args:
            url: The URL to fetch

        Returns:
            BeautifulSoup object of the parsed page
        """
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup

        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def search_terms_in_text(self, text: str, search_terms: List[str], case_sensitive: bool = False) -> Dict[str, List[str]]:
        """
        Search for terms in text and return matches with context.

        Args:
            text: Text to search in
            search_terms: List of terms to search for
            case_sensitive: Whether search should be case sensitive

        Returns:
            Dictionary with terms as keys and list of context snippets as values
        """
        results = {}

        for term in search_terms:
            matches = []

            # Prepare text and term for searching
            search_text = text if case_sensitive else text.lower()
            search_term = term if case_sensitive else term.lower()

            # Find all occurrences
            pattern = re.escape(search_term)
            for match in re.finditer(pattern, search_text):
                start = max(0, match.start() - 50)  # 50 characters before
                end = min(len(text), match.end() + 50)  # 50 characters after
                context = text[start:end].strip()

                # Clean up the context
                context = re.sub(r'\s+', ' ', context)  # Replace multiple whitespace with single space
                matches.append(context)

            if matches:
                results[term] = matches

        return results

    def scrape_urls(self, urls: List[str], search_terms: List[str],
                   case_sensitive: bool = False, search_in: str = 'all') -> Dict[str, Dict]:
        """
        Scrape multiple URLs and search for terms.

        Args:
            urls: List of URLs to scrape
            search_terms: List of terms to search for
            case_sensitive: Whether search should be case sensitive
            search_in: Where to search - 'all', 'title', 'body', 'links'

        Returns:
            Dictionary with URLs as keys and search results as values
        """
        results = {}

        for i, url in enumerate(urls):
            print(f"Scraping {i+1}/{len(urls)}: {url}")

            # Add delay between requests
            if i > 0:
                time.sleep(self.delay)

            soup = self.fetch_page(url)
            if soup is None:
                results[url] = {"error": "Failed to fetch page"}
                continue

            # Extract text based on search_in parameter
            text_to_search = ""

            if search_in == 'all' or search_in == 'title':
                title = soup.find('title')
                if title:
                    text_to_search += title.get_text() + " "

            if search_in == 'all' or search_in == 'body':
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()
                text_to_search += soup.get_text()

            if search_in == 'all' or search_in == 'links':
                links = soup.find_all('a')
                for link in links:
                    if link.get_text():
                        text_to_search += link.get_text() + " "
                    if link.get('href'):
                        text_to_search += link.get('href') + " "

            # Search for terms
            matches = self.search_terms_in_text(text_to_search, search_terms, case_sensitive)

            # Store results
            results[url] = {
                "matches": matches,
                "total_matches": sum(len(contexts) for contexts in matches.values()),
                "page_title": soup.find('title').get_text().strip() if soup.find('title') else "No title"
            }

        return results

    def print_results(self, results: Dict[str, Dict]):
        """
        Print search results in a formatted way.

        Args:
            results: Results dictionary from scrape_urls
        """
        print("\n" + "="*80)
        print("WEB SCRAPING RESULTS")
        print("="*80)

        for url, data in results.items():
            print(f"\nURL: {url}")

            if "error" in data:
                print(f"  ❌ {data['error']}")
                continue

            print(f"  📄 Title: {data['page_title']}")
            print(f"  🔍 Total matches: {data['total_matches']}")

            if data['matches']:
                print("  📝 Found terms:")
                for term, contexts in data['matches'].items():
                    print(f"    • '{term}' ({len(contexts)} occurrences)")
                    for i, context in enumerate(contexts[:3], 1):  # Show max 3 contexts per term
                        print(f"      {i}. ...{context}...")
                    if len(contexts) > 3:
                        print(f"      ... and {len(contexts) - 3} more occurrences")
            else:
                print("  ❌ No matches found")
