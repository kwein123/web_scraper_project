# Web Scraper Project

A simple, respectful web scraper built with Python and BeautifulSoup.

## Features

- **Respectful scraping**: Built-in delays between requests
- **Flexible search**: Search in titles, body text, or links
- **Context extraction**: Get surrounding text for matches
- **Multiple output formats**: Console output and JSON file export
- **Error handling**: Graceful handling of failed requests
- **Configurable**: Easy to customize URLs, terms, and settings

## Installation

### From PyPI (if published)
```bash
pip install web_scraper_project
```

### Development Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kwein123/web-scraper.git
   cd web-scraper
   ```

2. Install in development mode:
   ```bash
   pip install -e .
   ```

3. Or install with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Quick Start

### Command Line Usage
After installation, you can run the scraper directly:

```bash
web-scraper-project
# or
webscraper
```

### Python Usage
```python
from scraper import WebScraper

scraper = WebScraper(delay=1.0)
results = scraper.scrape_urls(
    urls=["https://example.com"],
    search_terms=["example", "test"]
)
scraper.print_results(results)
```

## File Structure

```
web_scraper_project/
├── scraper.py          # Main WebScraper class
├── config.py           # Configuration settings
├── main.py             # Main execution script
├── test_scraper.py     # Unit tests
├── example_usage.py    # Usage examples
├── requirements.txt    # Dependencies
├── setup.py           # Setup script
├── pyproject.toml     # Modern Python packaging
├── MANIFEST.in        # Package manifest
├── LICENSE            # MIT License
└── README.md          # This file
```

## Configuration

Edit `config.py` to customize:

```python
# URLs to scrape
URLS = [
    "https://example.com",
    "https://python.org"
]

# Terms to search for
SEARCH_TERMS = [
    "python",
    "programming",
    "example"
]

# Scraper settings
SCRAPER_DELAY = 1.0  # Delay between requests
CASE_SENSITIVE = False
SEARCH_IN = 'all'  # 'all', 'title', 'body', 'links'
```

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

### Case-Sensitive Search
```python
results = scraper.scrape_urls(
    urls=urls,
    search_terms=["Python", "PYTHON"],
    case_sensitive=True
)
```

### Custom Configuration
```python
scraper = WebScraper(delay=2.0)  # Longer delay for politeness
results = scraper.scrape_urls(
    urls=custom_urls,
    search_terms=custom_terms,
    case_sensitive=False,
    search_in='body'  # Search only in page body
)
```

## API Reference

### WebScraper Class

#### `__init__(delay: float = 1.0)`
Initialize the scraper with optional delay between requests.

#### `fetch_page(url: str) -> BeautifulSoup`
Fetch and parse a single web page.

#### `search_terms_in_text(text: str, search_terms: List[str], case_sensitive: bool = False) -> Dict[str, List[str]]`
Search for terms in text and return matches with context.

#### `scrape_urls(urls: List[str], search_terms: List[str], case_sensitive: bool = False, search_in: str = 'all') -> Dict[str, Dict]`
Scrape multiple URLs and search for terms.

#### `print_results(results: Dict[str, Dict])`
Print search results in a formatted way.

## Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=scraper

# Run specific test file
python test_scraper.py
```

## Development

### Setting up development environment
```bash
# Clone the repo
git clone https://github.com/kwein123/web-scraper.git
cd web-scraper

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run tests
python -m pytest

# Run linting
flake8 .

# Run type checking
mypy .

# Format code
black .
```

### Building the package
```bash
# Build source and wheel distributions
python -m build

# Upload to PyPI (requires account and setup)
python -m twine upload dist/*
```

## Important Notes

- **Respect robots.txt**: Always check and respect website robots.txt files
- **Rate limiting**: The scraper includes delays between requests to be respectful
- **Terms of service**: Some websites may block automated requests
- **Legal considerations**: Consider legal and ethical implications of web scraping
- **User agent**: The scraper sets a realistic user agent to avoid blocks

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is for educational purposes. Always ensure you have permission to scrape websites and comply with their terms of service and applicable laws.