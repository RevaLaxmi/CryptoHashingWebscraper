import requests
from bs4 import BeautifulSoup

#and then we want to import it to save it to a file.
import json
import csv

url = "https://bigdipper.live/quicksilver/accounts/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"

response = requests.get(url) #get req to url
soup = BeautifulSoup(response.content, 'html.parser') #parse html content

transactions_section = soup.find('div', class_='mui-style-1aqmhr2-root-root-transactions') #get the "Transaction" section

transaction_hashes = []
for T in transactions_section.find_all('div', class_='mui-style-1tbeysr-root'): #then we get the hashes from the section
    transaction_hash = T.text.strip()
    transaction_hashes.append(transaction_hash)

#just to check if its printing anything or scraping anything at all 
print("its not adding anything its empty:", transaction_hashes)

#this code is just to save it to the file.. whichever one we choose
with open('transaction_hashes.json', 'w') as json_file:
    json.dump(transaction_hashes, json_file, indent=5)

with open('transaction_hashes.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Transaction Hash'])
    writer.writerows([[hash] for hash in transaction_hashes])

#we should probably add a statement to check if empty and return that its not doing anythign but in this case we can just check
#print("Hash scraped and added to file")



# -------------------------------------------------------------------------------------------------------------------------------------# 

#now the HTML classes were taking after printing it out and checking the elements regardless 

"""
# we're getting this informatio from getting the basic HTML layout 

import requests
from bs4 import BeautifulSoup

url = "https://bigdipper.live/quicksilver/accounts/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

transaction_section = soup.find("div", class_="mui-style-1aqmhr2-root-root-transactions")

print(transaction_section.prettify())

"""
