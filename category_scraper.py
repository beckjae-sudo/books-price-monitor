import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"


def get_book_links(category_url):

    book_links = []

    current_page = category_url

    while current_page:

        response = requests.get(current_page)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            link = book.find("h3").find("a")["href"]

            if link.startswith("../../../"):
                link = link.replace("../../../", "")

            book_links.append(BASE_URL + "catalogue/" + link)

        # Look for next page
        next_button = soup.find("li", class_="next")

        if next_button:
            next_link = next_button.find("a")["href"]

            current_page = current_page.rsplit("/", 1)[0] + "/" + next_link

        else:
            current_page = None
            
        return book_links    

def get_category_links():

    url = "https://books.toscrape.com/"

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    categories = {}

    category_list = soup.find("ul", class_="nav nav-list").find_all("a")

    for category in category_list[1:]:

        name = category.text.strip()
        link = category["href"]

        categories[name] = "https://books.toscrape.com/" + link

    return categories