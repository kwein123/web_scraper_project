# =============================================================================
# FILE: README.md
# Project documentation
# =============================================================================

"""
# Web Scraper Project

A simple, respectful web scraper built with Python and BeautifulSoup.

## Installation

1. Install Python 3.7 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

Run the main script:
```bash
python main.py
```

## File Structure

- `scraper.py` - Main WebScraper class
- `config.py` - Configuration settings
- `main.py` - Main execution script
- `test_scraper.py` - Unit tests
- `example_usage.py` - Usage examples
- `requirements.txt` - Dependencies
- `README.md` - This file

## Usage Examples

### Basic Usage
```python
from scraper import WebScraper

scraper = WebScraper(delay=1.0)
results = scraper.scrape_urls(
    urls=["https://example.com"],
    search_terms=["example", "test"]
)
scraper.print_results(results)
```

### Search Only in Titles
```python
results = scraper.scrape_urls(
    urls=urls,
    search_terms=terms,
    search_in='title'
)
```

## Running Tests

```bash
python test_scraper.py
```

## Configuration

Edit `config.py` to customize:
- URLs to scrape
- Search terms
- Scraper settings (delay, case sensitivity, etc.)

## Important Notes

- Always respect robots.txt and website terms of service
- The scraper includes delays between requests to be respectful
- Some websites may block automated requests
- Consider legal and ethical implications of web scraping

## License

This project is for educational purposes. Use responsibly.
"""