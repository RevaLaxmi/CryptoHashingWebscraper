import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.mintscan.io/quicksilver/account/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the <a> tags with class "T×Card_link"
hash_links = soup.find_all("a", class_="T×Card_link")

# Extract the transaction hash values from the <a> tags
hash_numbers = [hash_link.text.strip() for hash_link in hash_links]

# Print the transaction hash values
for hash_number in hash_numbers:
    print(hash_number)
