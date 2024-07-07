import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage and retrieve the HTML content
url = "https://bigdipper.live/quicksilver/accounts/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the transactions section by class name
transactions_section = soup.find("div", class_="Transactions")

# Remove elements from the transactions section based on criteria (e.g., remove elements with "Hash" value)
if transactions_section:
    for transaction in transactions_section.find_all("div", class_="Hash"):
        transaction.decompose()

# Print the modified HTML content
print(soup.prettify())
