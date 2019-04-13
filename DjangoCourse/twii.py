import requests

url = 'http://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20190412&selectType=ALL'
data = requests.get(url).text
print(data)
