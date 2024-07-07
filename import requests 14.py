import requests
from bs4 import BeautifulSoup

url = "https://bigdipper.live/quicksilver/accounts/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

transaction_section = soup.find("div", class_="mui-style-1aqmhr2-root-root-transactions")
transaction_hashes = transaction_section.find_all("p", class_="MuiTypography-root MuiTypography-body1 value mui-style-nqa33h")

for hash_element in transaction_hashes:
    hash_value = hash_element.find("a").text
    print(hash_value)
