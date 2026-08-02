from category_scraper import get_category_links, get_book_links
from scraper import scrape_book
from csv_writer import write_books_to_csv

from image_downloader import download_image

categories = get_category_links()


print(f"Found {len(categories)} categories")


for category_name, category_url in categories.items():

    print(f"\nProcessing category: {category_name}")

    book_links = get_book_links(category_url)

    print(f"Found {len(book_links)} books")

    books = []

    for link in book_links:

        print(f"Scraping: {link}")

        book = scrape_book(link)

        download_image(
            book["image_url"],
            book["book_title"]
        )

        books.append(book)


    filename = f"data/{category_name.lower().replace(' ', '-')}.csv"

    write_books_to_csv(filename, books)

    print(f"Created: {filename}")


print("\nAll categories completed!")

