#!/usr/bin/env python3
"""
Command-line interface for the web scraper.
"""

import argparse
import sys
import json
from datetime import datetime
from .scraper import WebScraper
from . import config


def save_results_to_file(results, filename=None):
    """Save results to a JSON file."""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"scraper_results_{timestamp}.json"

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Results saved to: {filename}")
        return filename
    except Exception as e:
        print(f"\n❌ Error saving results: {e}")
        return None


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Web Scraper - A respectful web scraping tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    # Use config.py settings
  %(prog)s --urls https://example.com         # Single URL
  %(prog)s --terms python web --delay 2.0     # Custom terms and delay
  %(prog)s --config-only                      # Show current configuration
  %(prog)s --examples                         # Run example scenarios
        """
    )

    parser.add_argument(
        '--urls',
        nargs='+',
        help='URLs to scrape (overrides config.py)'
    )

    parser.add_argument(
        '--terms',
        nargs='+',
        help='Search terms (overrides config.py)'
    )

    parser.add_argument(
        '--delay',
        type=float,
        help='Delay between requests in seconds'
    )

    parser.add_argument(
        '--case-sensitive',
        action='store_true',
        help='Make search case sensitive'
    )

    parser.add_argument(
        '--search-in',
        choices=['all', 'title', 'body', 'links'],
        help='Where to search for terms'
    )

    parser.add_argument(
        '--output',
        help='Output file for results (JSON format)'
    )

    parser.add_argument(
        '--config-only',
        action='store_true',
        help='Show current configuration and exit'
    )

    parser.add_argument(
        '--examples',
        action='store_true',
        help='Run example scenarios'
    )

    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {get_version()}'
    )

    args = parser.parse_args()

    # Show configuration only
    if args.config_only:
        show_configuration()
        return

    # Run examples
    if args.examples:
        run_examples()
        return

    # Use command line args or fall back to config
    urls = args.urls or getattr(config, 'URLS', ['https://example.com'])
    search_terms = args.terms or getattr(config, 'SEARCH_TERMS', ['example'])
    delay = args.delay if args.delay is not None else getattr(config, 'SCRAPER_DELAY', 1.0)
    case_sensitive = args.case_sensitive or getattr(config, 'CASE_SENSITIVE', False)
    search_in = args.search_in or getattr(config, 'SEARCH_IN', 'all')

    print("🔍 Web Scraper Starting...")
    print(f"📝 URLs to scrape: {len(urls)}")
    print(f"🔎 Search terms: {search_terms}")
    print(f"⏱️  Delay between requests: {delay}s")
    print(f"🔤 Case sensitive: {case_sensitive}")
    print(f"📍 Search in: {search_in}")
    print("-" * 50)

    # Initialize and run scraper
    scraper = WebScraper(delay=delay)

    try:
        results = scraper.scrape_urls(
            urls=urls,
            search_terms=search_terms,
            case_sensitive=case_sensitive,
            search_in=search_in
        )

        # Print results
        scraper.print_results(results)

        # Save results
        output_file = save_results_to_file(results, args.output)

        print(f"\n✅ Scraping completed successfully!")
        if output_file:
            print(f"📁 Results saved to: {output_file}")

    except KeyboardInterrupt:
        print("\n⚠️  Scraping interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during scraping: {e}")
        sys.exit(1)


def show_configuration():
    """Display current configuration."""
    print("📋 Current Configuration:")
    print("=" * 50)

    try:
        print(f"URLs: {getattr(config, 'URLS', 'Not set')}")
        print(f"Search Terms: {getattr(config, 'SEARCH_TERMS', 'Not set')}")
        print(f"Delay: {getattr(config, 'SCRAPER_DELAY', 'Not set')} seconds")
        print(f"Case Sensitive: {getattr(config, 'CASE_SENSITIVE', 'Not set')}")
        print(f"Search In: {getattr(config, 'SEARCH_IN', 'Not set')}")
    except Exception as e:
        print(f"Error reading configuration: {e}")

    print("\n💡 To customize, edit the config.py file or use command-line arguments.")


def run_examples():
    """Run example scenarios."""
    print("🚀 Running Example Scenarios...")
    try:
        from .examples import (
            example_basic_usage,
            example_title_only_search,
            example_case_sensitive,
            example_custom_search
        )

        examples = [
            ("Basic Usage", example_basic_usage),
            ("Title-Only Search", example_title_only_search),
            ("Case-Sensitive Search", example_case_sensitive),
            ("Custom Search", example_custom_search),
        ]

        for name, example_func in examples:
            print(f"\n{'='*60}")
            print(f"Running: {name}")
            print('='*60)
            try:
                example_func()
            except Exception as e:
                print(f"❌ Example failed: {e}")

    except ImportError as e:
        print(f"❌ Could not import examples: {e}")


def get_version():
    """Get package version."""
    try:
        from . import __version__
        return __version__
    except ImportError:
        return "unknown"


if __name__ == "__main__":
    main()