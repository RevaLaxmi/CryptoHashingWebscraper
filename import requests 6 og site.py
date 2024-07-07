import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.mintscan.io/quicksilver/account/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the anchor tags with class "T×Card_link" that contain hash numbers
hash_links = soup.find_all("a", class_="T×Card_link")

# Extract the hash numbers from the anchor tags
hash_numbers = [link.get_text(strip=True) for link in hash_links]

# Print the hash numbers
for hash_number in hash_numbers:
    print(hash_number)
