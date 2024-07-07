const axios = require('axios');

async function getTransactionDetails(transactionHash) {
  try {
    // Construct the URL to query the blockchain for transaction details
    const url = `https://rpc-1.quicksilver.nodes.guru/tx_search?query="tx.hash='${transactionHash}'"`;

    // Make an HTTP GET request to the blockchain API
    const response = await axios.get(url);

    // Check if the response contains valid data and if the transaction is found
    if (!response.data || !response.data.result || response.data.result.total_count === '0') {
      console.log('Transaction not found.');
      return;
    }

    // Extract transaction details from the response
    const transaction = response.data.result.txs[0];
    const { height, timestamp } = transaction;

    // Output the transaction details to the console
    console.log('Transaction Details:');
    console.log('-------------------');
    console.log('Transaction Hash:', transactionHash);
    console.log('Height:', height);
    console.log('Timestamp:', timestamp);
  } catch (error) {
    // Handle and log any errors that occur during the process
    console.error('Error:', error.message);
  }
}

// the transaction hash
const transactionHash = 'EE1EA092DDC65AF12F6867192A26178C6E99BFC33D6AC24442E33A79A8BD69DE';

// calling the function
getTransactionDetails(transactionHash);