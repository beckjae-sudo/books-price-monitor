import os
import csv



def write_books_to_csv(filename, books):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.DictWriter(
            csvfile,
            fieldnames=books[0].keys()
        )

        writer.writeheader()
        writer.writerows(books)