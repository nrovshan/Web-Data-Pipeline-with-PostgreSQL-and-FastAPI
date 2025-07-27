import requests
from bs4 import BeautifulSoup
import pandas as pd


# Define a function to scrape book information from a range of pages
def scrape_pages(start_page: int, end_page: int):

    # Base URL of the book site with a placeholder for page numbers
    base_url = "https://books.toscrape.com/"
    main_url = base_url + "catalogue/page-{}.html"

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
            
            # Get detail page link (fix relative URL)
            detail_partial_url = book.h3.a["href"]
            detail_url = base_url + "catalogue/" + detail_partial_url.replace('../../../', '')

            # Visit book detail page
            detail_response = requests.get(detail_url)
            detail_soup = BeautifulSoup(detail_response.content, "html.parser")
            stock = detail_soup.find("p", class_="instock availability").get_text(strip=True)

            category = detail_soup.find_all("ul", class_ = "breadcrumb")[0].find_all("a")[2].text

            book_tax = detail_soup.find("th", string="Tax").find_next_sibling("td").text.strip()

            number_reviews = detail_soup.find("th", string="Number of reviews").find_next_sibling("td").text.strip()


            page_url = detail_url


            # Append the extracted data as a tuple to the book list
            book_list.append((
                title,
                price,
                stars,
                stock,
                category,
                book_tax,
                number_reviews,
                page_url
            ))
            
    # Return the final list of books
    return book_list


    


