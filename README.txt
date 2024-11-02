# Web Scraper

This Python script is a simple web scraper that extracts and lists up to 100 unique hyperlinks from a given webpage. It uses the `urllib` library for making HTTP requests and `BeautifulSoup` from the `bs4` module for parsing HTML content.

## Features

- Accepts a URL as input from the user.
- Retrieves all hyperlinks (`<a>` tags) from the specified webpage.
- Follows the found links to extract additional hyperlinks.
- Limits the results to a maximum of 100 unique HTTP links.

## Prerequisites

- Python 3.x
- Libraries:
  - `urllib`
  - `BeautifulSoup4`

You can install the required libraries using pip:

```bash
pip install beautifulsoup4
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
