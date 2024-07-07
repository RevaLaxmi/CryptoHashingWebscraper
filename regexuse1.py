import re

# url = 'https://rpc-1.quicksilver.nodes.guru/tx_search?query="tx.hash=\'EE1EA092DDC65AF12F6867192A26178C6E99BFC33D6AC24442E33A79A8BD69DE\'"&query="tx.hash=\'F2C3B4139D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2\'"'

url = 'https://bigdipper.live/quicksilver/accounts/quick17mhgd2v4f6ut65m343g6fza45a28n3ff0lg7uj' 

pattern = r'\b[A-Za-z0-9]{64}\b'
matches = re.findall(pattern, url)

if len(matches) > 0:
    for x in matches:
        print(x)
else:
    print("NULL")
