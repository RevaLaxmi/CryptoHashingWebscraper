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
    hash_elements = transactions_section.find_all("p")
    for hash_element in hash_elements:
        hash_number = hash_element.text.strip()
        if hash_number.startswith("Hash"):
            hash_numbers.append(hash_number.split(":")[1].strip())

# Print the extracted hash numbers
for hash_number in hash_numbers:
    print(hash_number)
