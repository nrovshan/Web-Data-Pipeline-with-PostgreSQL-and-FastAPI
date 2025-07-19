import requests
from bs4 import BeautifulSoup
import pandas as pd


# Define a function to scrape book information from a range of pages
def scrape_pages(start_page: int, end_page: int):

    # Base URL of the book site with a placeholder for page numbers
    main_url = "http://books.toscrape.com/catalogue/page-{}.html"

    # Initialize an empty list to hold book data
    book_list = []

    # Loop through the specified range of pages
    for page_num in range(start_page, end_page + 1):

        url = main_url.format(page_num)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.find_all("article", class_="product_pod")


        # Loop through each book element found
        for book in books:

            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip()
            star_tag = book.find("p", class_="star-rating")
            stars = star_tag["class"][1] 
            stock = book.find("p", class_="instock availability").text.strip()


            # Append the extracted data as a tuple to the book list
            book_list.append((
                title,
                price,
                stars,
                stock
            ))
            
    # Return the final list of books
    return book_list
    



