## Price Scraper + Currency Converter

## 1. Project Overview

This project is a Python-based web scraping application that extracts book titles and prices from an online bookstore (Books to Scrape), retrieves currency exchange rates through an API, and converts the prices from British Pounds (GBP) to Kenyan Shillings (KES).

## 2. Project Objectives

- Practise web scraping using Python.
- Extract product names and prices from a website.
- Integrate a currency conversion API.
- Convert prices from GBP to KES.
- Organise and export collected data into a CSV file.

## 3. Features

- Scrapes book titles and prices using Requests and BeautifulSoup.
- Extracts 20 books from the website.
- Cleans extracted prices and converts them into numerical values.
- Retrieves GBP-to-KES exchange rates using ExchangeRate-API.
- Converts book prices into Kenyan Shillings.
- Displays the results in a structured table using Pandas.
- Exports the results into a CSV file.
- Includes error handling for connection issues.

## 4. Technologies and Libraries Used

- Python
- Requests
- BeautifulSoup (BeautifulSoup4)
- Pandas
- ExchangeRate-API

## 5. Data Sources

- Books to Scrape: https://books.toscrape.com/
- ExchangeRate-API: https://www.exchangerate-api.com/

## 6. Project Files

| File | Description |
|---|---|
| `price_scraper.py` | Main Python script for scraping and currency conversion |
| `book_prices_converted.csv` | Output file containing book titles and converted prices |
| `requirements.txt` | List of required Python libraries |
| `README.md` | Project documentation |

## 7. How to Run the Application

**Step 1: Install the required libraries**

```bash
pip install -r requirements.txt
```

**Step 2: Run the Python script**

```bash
python price_scraper.py
```

**Step 3: View the output**

The application displays the scraped book titles, original GBP prices and converted KES prices in the terminal.

The results are also saved in `book_prices_converted.csv`, which can be opened using Microsoft Excel or other spreadsheet applications.

## 8. Expected Output

The generated dataset contains the following columns:

- Book Title
- Price (GBP)
- Price (KES)

## 9. Error Handling

The application uses Python exception handling (`try` and `except`) to manage website connection failures and currency API errors.

