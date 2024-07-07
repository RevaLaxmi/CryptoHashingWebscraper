import requests
import json
import csv
from bs4 import BeautifulSoup

url = "https://www.mintscan.io/quicksilver/account/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj"

# Send a GET request to the website
response = requests.get(url)

# Create BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Find the Transactions section
transactions_section = soup.find('div', class_='table-responsive')

if transactions_section is not None:
    # Find all the TxHash values
    txhashes = transactions_section.find_all('td', class_='text-truncate hash')

    # Create a list to store the TxHash values
    txhash_list = []

    # Extract the TxHash values and add them to the list
    for txhash in txhashes:
        txhash_list.append(txhash.text.strip())

    # Save the TxHash values to a JSON file
    with open('txhashes.json', 'w') as json_file:
        json.dump(txhash_list, json_file)

    # Save the TxHash values to a CSV file
    with open('txhashes.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['TxHash'])
        writer.writerows([[txhash] for txhash in txhash_list])

    print("TxHash values scraped and saved successfully.")
else:
    print("Transactions section not found on the webpage.")
