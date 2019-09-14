import requests
from bs4 import BeautifulSoup
stockcode = "ASIANPAINT"
stock_code = stockcode
stock_url  = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stock_code)
response = requests.get(stock_url)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')
data_array = soup.find(id='responseDiv').getText().strip().split(":")
print(data_array)   #just for cross check
for item in data_array:
    if 'lastPrice' in item:
        index = data_array.index(item)+1
        print("Index -> "+ str(index))
        latestPrice=data_array[index].split('"')[1]
        print(latestPrice)