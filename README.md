# Books Price Monitor

## Overview

Books Price Monitor is a Python web-scraping application that extracts book information from [Books to Scrape](https://books.toscrape.com/).

The application can:

* Extract information from individual book pages
* Scrape all books within a category
* Automatically handle category pagination
* Scrape all available book categories
* Save each category's data to a separate CSV file
* Download and save the cover image for each book

### Data Collected

For each book, the application extracts:

* Product page URL
* Universal Product Code (UPC)
* Book title
* Price including tax
* Price excluding tax
* Quantity available
* Product description
* Category
* Review rating
* Image URL

## Requirements

* Python 3.14 or compatible Python 3 version
* Internet connection
* The Python packages listed in `requirements.txt`

## Installation

### 1. Clone the Repository

Clone the repository from GitHub and navigate into the project directory:

```powershell
git clone https://github.com/beckjae-sudo/books-price-monitor.git
cd books-price-monitor
```

### 2. Create a Virtual Environment

Create a Python virtual environment:

```powershell
py -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate
```

The terminal should then show `(.venv)` before the command prompt.

### 4. Install Dependencies

Install the required Python packages:

```powershell
py -m pip install -r requirements.txt
```

## Running the Application

With the virtual environment activated, run:

```powershell
py main.py
```

The application will:

1. Retrieve all available book categories.
2. Find all books within each category.
3. Automatically follow pagination when additional category pages exist.
4. Extract the required product information.
5. Download the associated book cover images.
6. Save the book data as CSV files.

## Output

CSV files are saved in:

```text
data/
```

Book cover images are saved in:

```text
images/
```

The `data` and `images` directories are intentionally excluded from Git because they contain generated output.

## Project Structure

```text
books-price-monitor/
│
├── category_scraper.py
├── csv_writer.py
├── image_downloader.py
├── main.py
├── parser.py
├── scraper.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/          # Generated CSV files
└── images/        # Downloaded book images
```

## Git

The project uses Git for version control. The virtual environment and generated output files are excluded from the repository using `.gitignore`.
