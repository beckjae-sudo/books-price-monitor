import requests
from bs4 import BeautifulSoup

def scrape_book(url):

    response = requests.get(url)
    response.encoding = "utf-8"
    response.raise_for_status()

# Parse HTML
    soup = BeautifulSoup(response.text, "lxml")

# -----------------------------
# Basic Product Information
# -----------------------------

    product_page_url = url

    book_title = soup.find("h1").text.strip()

# -----------------------------
# Product Information Table
# -----------------------------

    product_info = {}

    rows = soup.find_all("tr")

    for row in rows:
        key = row.find("th").text.strip()
        value = row.find("td").text.strip()
        product_info[key] = value

    
    upc = product_info["UPC"]
    price_including_tax = product_info["Price (incl. tax)"]
    price_including_tax = product_info["Price (incl. tax)"]
    price_excluding_tax = product_info["Price (excl. tax)"]
    quantity_available = product_info["Availability"]

# -----------------------------
# Product Description
# -----------------------------

    description_header = soup.find("div", id="product_description")

    if description_header:
        product_description = description_header.find_next("p").text.strip()
    else:
        product_description = ""

# -----------------------------
# Category
# -----------------------------

    category = soup.find("ul", class_="breadcrumb").find_all("a")[-1].text.strip()

# -----------------------------
# Review Rating
# -----------------------------

    review_rating = soup.find("p", class_="star-rating")["class"][1]

# -----------------------------
# Image URL
# -----------------------------

    image = soup.find("div", class_="item active").find("img")

    image_url = "https://books.toscrape.com/" + image["src"].replace("../../", "")

# -----------------------------
# Return the scraped data
# -----------------------------

    return {
    "product_page_url": product_page_url,
    "universal_product_code": upc,
    "book_title": book_title,
    "price_including_tax": price_including_tax,
    "price_excluding_tax": price_excluding_tax,
    "quantity_available": quantity_available,
    "product_description": product_description,
    "category": category,
    "review_rating": review_rating,
    "image_url": image_url,
    }
    return book
