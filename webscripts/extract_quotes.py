import requests
from bs4 import BeautifulSoup
import urllib.parse


def main():
    token = "0f5f933302d34859add35ea3dadf4fd57e622084943"
    target_url = urllib.parse.quote(
        "https://www.brainyquote.com/profession/quotes-by-leaders")  # Replace with the URL of your choice
    url = "http://api.scrape.do?token={}&url={}".format(token, target_url)

    try:
        # Send an HTTP GET request and retrieve the HTML content
        response = requests.request("GET", url)
        response.raise_for_status()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        # print(soup.prettify())
        # Define the CSS selector to target the book elements
        quotes_selector = ".b-qt"  # Replace with the appropriate CSS selector

        # Find all elements that match the CSS selector
        quotes = soup.select(quotes_selector)
        # print(quotes)
        print(quotes[0].getText())
        print(len(quotes))
        # print(quotes)
        # for quote in quotes:
        #     line = quote.select_one(".b-qt").getText  # Replace with the appropriate CSS selector
        #         author = book.select_one(".book-author").get_text()  # Replace with the appropriate CSS selector
        #         price = book.select_one(".book-price").get_text()  # Replace with the appropriate CSS selector
        #
        #         # Print the extracted book data
        #     print("Quote:", line)
    #         print("Author:", author)
    #         print("Price:", price)
    #         print("--------------------")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
