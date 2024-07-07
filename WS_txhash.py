"""
send http req
get the html stuff -> we have the get what we actually want so use bs4
store the data json/spreadsheet/csv file
"""

# The web scraper initiates an HTTP GET or POST request to the target URL 
import requests
# parse the HTML and create a structured representation of the document.
from bs4 import BeautifulSoup

def scrape_transaction_data(url):
    response = requests.get(url)
    
    #check successfull response 
    if response.status_code == 200: 
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # put the correct container element for the transactions
        transactions_container = soup.find('div', class_='Transactions')
        
        # Find all transaction rows within the container
        transaction_rows = transactions_container.find_all('div', class_='Transactions')
        
        transaction_data = []
        
        for row in transaction_rows:
            # Extract the desired data from each transaction row - just tx hash in this case
            Hash = row.find('span', class_='Hash').text
            

            # Store the transaction data in a dictionary or data structure of your choice
            Transactions = {
                'Hash': Hash
                
            }
            
            transaction_data.append(Transactions)
        
        return transaction_data
    
    else:
        print("Failed to retrieve the webpage. Error code:", response.status_code)
        return []

# Example usage:
url = 'https://bigdipper.live/quicksilver/accounts/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj'
Transactions = scrape_transaction_data(url)

for transaction in Transactions:
    print("Transaction Hash:", transaction['Hash'])
    '''
    print("Sender:", transaction['sender'])
    print("Receiver:", transaction['receiver'])
    print("Amount:", transaction['amount'])
    '''
    print()
