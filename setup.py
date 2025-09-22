#!/usr/bin/env python3
"""
Setup script for web-scraper package.
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    """Read README.md file for long description."""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "A simple, respectful web scraper built with Python and BeautifulSoup."

# Read requirements from requirements.txt
def read_requirements():
    """Read requirements.txt file."""
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    requirements = []
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Skip comments and empty lines
                if line and not line.startswith('#') and not line.startswith('='):
                    # Extract just the package name and version
                    if '>=' in line:
                        requirements.append(line)
                    elif '==' in line:
                        requirements.append(line.replace('==', '>='))
                    else:
                        requirements.append(line)
    return requirements

setup(
    name="web_scraper_project",
    version="1.0.2",
    author="Kevin Weinrich",
    author_email="weinrichkevin@gmail.com",
    description="A simple, respectful web scraper built with Python and BeautifulSoup",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/kwein123/web_scraper_project",
    #packages=find_packages(),
    py_modules=[
        'scraper',
        'config',
        'main',
        'example_usage'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        #"License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "progress": [
            "tqdm>=4.66.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "web_scraper_project=main:main",
            "webscraper=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="web scraping, beautifulsoup, html parsing, data extraction",
    project_urls={
        "Bug Reports": "https://github.com/kwein123/web_scraper_project/issues",
        "Source": "https://github.com/kwein123/web_scraper_project",
        "Documentation": "https://github.com/kwein123/web_scraper_project#readme",
    },
)