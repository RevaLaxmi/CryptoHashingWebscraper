import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.mintscan.io/quicksilver/txs/EE1EA092DDC65AF12F6867192A26178C6E99BFC33D6AC24442E33A79A8BD69DE?height=1947286"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the <div> tags with class "InfoRow value"
hash_divs = soup.find_all("div", class_="InfoRow value")

# Extract the transaction hash values from the <div> tags
hash_numbers = [hash_div.text.strip() for hash_div in hash_divs]

# Print the transaction hash values
for hash_number in hash_numbers:
    print(hash_number)
