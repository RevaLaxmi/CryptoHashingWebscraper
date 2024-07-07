import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.mintscan.io/quicksilver/account/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the div tags with class "Card_cardHeader_"
card_headers = soup.find_all("div", class_="Card_cardHeader_")

# Extract the transaction hash (TxHash) values from the card headers
tx_hashes = []
for card_header in card_headers:
    tx_hash = card_header.find("a", class_="T×Card_link")
    if tx_hash is not None:
        tx_hashes.append(tx_hash.get_text(strip=True))

# Print the transaction hash (TxHash) values
for tx_hash in tx_hashes:
    print(tx_hash)
