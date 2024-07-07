const axios = require('axios');

async function getTransactionDetails(transactionHash) {
  try {
    const url = 'https://rpc-1.quicksilver.nodes.guru/tx_search?query="tx.hash=\'' + transactionHash + '\'"';
    console.log
    const response = await axios.get(url);

    // Check if the transaction is found
    if (!response.data || !response.data.result || response.data.result.total_count === '0') {
      console.log('Transaction not found.');
      return;
    }


    // Extract transaction details
    const transaction = response.data.result.txs[0];
    console.log(transaction)
    const height = transaction.height;
    const timestamp = transaction.timestamp;

    console.log('Transaction Details:');
    console.log('-------------------');
    console.log('Transaction Hash:', transactionHash);
    console.log('Height:', height);
    console.log('Timestamp:', timestamp);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

const transactionHash = 'EE1EA092DDC65AF12F6867192A26178C6E99BFC33D6AC24442E33A79A8BD69DE';
getTransactionDetails(transactionHash);