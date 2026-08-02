import os
import requests


def download_image(image_url, book_title):

    # Make sure the images folder exists
    os.makedirs("images", exist_ok=True)

    # Create a safe filename
    filename = "".join(
        c for c in book_title if c.isalnum() or c in (" ", "-", "_")
    ).rstrip()

    image_path = os.path.join("images", filename + ".jpg")

    response = requests.get(image_url)
    response.raise_for_status()

    with open(image_path, "wb") as file:
        file.write(response.content)

    print(f"Downloaded image: {filename}")