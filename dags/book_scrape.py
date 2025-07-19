import requests
from bs4 import BeautifulSoup
import pandas as pd



def scrape_pages(start_page: int, end_page: int):

    main_url = "http://books.toscrape.com/catalogue/page-{}.html"

    book_list = []

    for page_num in range(start_page, end_page + 1):

        url = main_url.format(page_num)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.find_all("article", class_="product_pod")


        for book in books:

            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip()
            star_tag = book.find("p", class_="star-rating")
            stars = star_tag["class"][1] 
            stock = book.find("p", class_="instock availability").text.strip()

            book_list.append((
                title,
                price,
                stars,
                stock
            ))
            
            # df = pd.DataFrame(book_list, columns = ["title", "price", "stars", "stock"])

    return book_list
    



