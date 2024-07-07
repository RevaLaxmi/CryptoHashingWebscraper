import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.mintscan.io/quicksilver/account/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the parent element that contains the transaction hash values
parent_element = soup.find("div", class_="AccountTsBody_accountTxsListContainer_18XF8")

# Check if the parent element exists
if parent_element:
    # Find all the elements that contain the transaction hash values
    hash_elements = parent_element.find_all("a", class_="T×Card_link")

    # Extract the transaction hash values
    hash_numbers = [hash_element.text.strip() for hash_element in hash_elements]

    # Print the transaction hash values
    for hash_number in hash_numbers:
        print(hash_number)
else:
    print("Parent element not found.")

