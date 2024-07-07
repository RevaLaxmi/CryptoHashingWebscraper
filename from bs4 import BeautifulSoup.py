# 1

from bs4 import BeautifulSoup

html = """
<div class="mui-style-1aqmhr2-root-root-transactions">
  <h2 class="MuiTypography-root MuiTypography-h2 mui-style-8iyl5q">Transactions</h2>
  <div class="mui-style-1o2kqtb-list">
    <div class="mui-style-jfwfsb-root-hiddenUntilLg">
      <div style="overflow: visible; height: 0px; width: 0px;"></div>
    </div>
    <div class="mui-style-14kkyas-root-hiddenWhenLg">
      <div style="overflow: visible; height: 0px; width: 0px;">
        <div class="List" style="position: relative; height: 504px; width: 428px; overflow: auto; will-change: transform; direction: ltr;">
          <div style="height: 4906px; width: 100%;">
            <div style="position: absolute; left: 0px; top: 1455px; height: 291px; width: 100%;">
              <div>
                <div class="mui-style-16gjaz6-root">
                  <div class="mui-style-1rlyamu-item">
                    <h4 class="MuiTypography-root MuiTypography-h4 label mui-style-8humvj">Block</h4>
                    <a href="/quicksilver/blocks/1579857">1,579,857</a>
                  </div>
                  <div class="mui-style-1rlyamu-item">
                    <h4 class="MuiTypography-root MuiTypography-h4 label mui-style-8humvj">Hash</h4>
                    <p class="MuiTypography-root MuiTypography-body1 value mui-style-nqa33h"><a href="/quicksilver/transactions/7909713FD6B0B6BAF6DF2DCA37FF75DD0C2F0E4F0CAD20D198BEF566A975C538">7909713FD6B0B6BAF6DF2DCA37FF75DD0C2F0E4F0CAD20D198BEF566A975C538</a></p>
                  </div>
                  
                  <!-- More transaction blocks and hashes from the html element would be here and so on..-->
                  
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
"""

# this we're printing straight from the HTML layout to make sure we're getting the Hash we want 
soup = BeautifulSoup(html, 'html.parser')
transaction_blocks = soup.find_all('div', class_='mui-style-16gjaz6-root')

for block in transaction_blocks:
    block_number = block.find('a').text
    transaction_hash = block.find('p').find('a').text
    # I mean we could.. but don't need it right now
    # print("Block:", block_number)
    print("Hash:", transaction_hash)
    
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
