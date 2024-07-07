import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage and retrieve the HTML content
url = "https://bigdipper.live/quicksilver/accounts/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the transactions section by class name
transactions_section = soup.find("div", class_="mui-style-1aqmhr2-root-root-transactions")

# Extract the hash numbers from the transactions section
hash_numbers = []
if transactions_section:
    hash_elements = transactions_section.find_all("p", class_="MuiTypography-root MuiTypography-body1 value mui-style-na33h")
    hash_numbers = [hash_element.text.strip() for hash_element in hash_elements]

# Print the extracted hash numbers
for hash_number in hash_numbers:
    print(hash_number)
