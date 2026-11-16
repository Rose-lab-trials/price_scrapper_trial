
# PRICE SCRAPER + CURRENCY CONVERTER

import requests
from bs4 import BeautifulSoup
import pandas as pd

# STEP 1

url = "https://books.toscrape.com/"

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    # Create an empty list to store book information
    book_data = []

    # Extract the title and price of each book
    for book in books:

        title = book.h3.a["title"]

        price_text = book.find("p", class_="price_color").get_text(strip=True)

        # Remove the pound sign and convert price into a number
        price = float(price_text.replace("£", "").replace("Â", ""))

        book_data.append({
            "Book Title": title,
            "Price (GBP)": price
        })

    print("Successfully scraped", len(book_data), "books.")

except requests.exceptions.RequestException as error:
    print("Website connection error:", error)
    book_data = []


# ---------------------------------
# STEP 2: GET CURRENCY EXCHANGE RATE
# ---------------------------------

if len(book_data) >= 10:

    currency_url = "https://open.er-api.com/v6/latest/GBP"

    try:
        currency_response = requests.get(currency_url, timeout=15)
        currency_response.raise_for_status()

        currency_data = currency_response.json()

        if currency_data["result"] != "success":
            raise ValueError("Currency API did not return a successful result.")

        exchange_rate = currency_data["rates"]["KES"]

        print("Exchange rate: 1 GBP =", exchange_rate, "KES")

        # ---------------------------------
        # STEP 3: CONVERT GBP TO KES
        # ---------------------------------

        for book in book_data:
            book["Price (KES)"] = round(
                book["Price (GBP)"] * exchange_rate, 2
            )

        # ---------------------------------
        # STEP 4: CREATE A DATAFRAME
        # ---------------------------------

        df = pd.DataFrame(book_data)

        # Display the results
        print("\nBOOK PRICES IN GBP AND KES")
        print(df.to_string(index=False))

        # ---------------------------------
        # STEP 5: SAVE DATA TO CSV
        # ---------------------------------

        df.to_csv("book_prices_converted.csv", index=False)

        print("\nData successfully saved to book_prices_converted.csv")

        print("\nCurrency data source: https://www.exchangerate-api.com")

    except (requests.exceptions.RequestException, KeyError, ValueError) as error:
        print("Currency conversion error:", error)

else:
    print("Scraping unsuccessful or fewer than 10 books were collected.")
