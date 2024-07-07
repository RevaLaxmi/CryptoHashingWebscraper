import requests
from bs4 import BeautifulSoup

url = "https://bigdipper.live/quicksilver/accounts/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the transactions section
transactions_section = soup.find("div", class_="mui-style-1aqmhr2-root-root-transactions")

# Find all the transaction hash elements
hash_elements = transactions_section.find_all("a", href=True)

# Extract the transaction hashes
tx_hashes = [element["href"].split("/")[-1] for element in hash_elements]

# Print the transaction hashes
for tx_hash in tx_hashes:
    print(tx_hash)
