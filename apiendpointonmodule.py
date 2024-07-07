# to send HTTP requests
import requests


# Setting up the API endpoint and headers:
url = 'https://www.mintscan.io/quicksilver/txs/EE1EA092DDC65AF12F6867192A26178C6E99BFC33D6AC24442E33A79A8BD69DE?height=1947286'

# Set any required headers
headers = {
    'Authorization': 'Bearer YOUR_TOKEN', 'Content-Type': 'application/json'
}

# Send the GET request to the API endpoint
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Retrieve the response data in JSON format
    data = response.json()

    # Extract the required information
    chain_id = data['chain_id']
    tx_hash = data['tx_hash']
    status = data['status']
    height = data['height']
    time = data['time']
    fee = data['fee']
    gas_used = data['gas_used']
    gas_wanted = data['gas_wanted']
    memo = data['memo']

    # Print the collected data
    print("Chain ID:", chain_id)
    print("Transaction Hash:", tx_hash)
    print("Status:", status)
    print("Height:", height)
    print("Time:", time)
    print("Fee:", fee)
    print("Gas (used / wanted):", gas_used, "/", gas_wanted)
    print("Memo:", memo)
else:
    print('Error:', response.status_code)
