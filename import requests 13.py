# 2

import requests
from bs4 import BeautifulSoup

url = "https://bigdipper.live/quicksilver/accounts/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"
# so we'll use this link over the cosmos one because the scroll does make a difference, we don't have to use seperate web urls.. just this one

response = requests.get(url)

#print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

# The transaction section on the page comes under this class
transactions_section = soup.find("div", class_="mui-style-1aqmhr2-root-root-transactions")
# the items we need to select from come under....
transaction_items = transactions_section.find_all("div", class_="mui-style-1rlyamu-item")

# create a list to append to
hash_list = []

for item in transaction_items:
    # it's probably this class that's wrong from what I've found in the HTML elements of the site
    hash_element = item.find("p", class_="MuiTypography-root MuiTypography-body1 value mui-style-nqa33h")
    
    # because it's not appending anything here
    if hash_element:
        Hash = hash_element.find("a").text
        hash_list.append(Hash)

print(hash_list)



