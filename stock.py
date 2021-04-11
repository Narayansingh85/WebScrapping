from bs4 import BeautifulSoup
import time
import requests

html_cont = requests.get('https://www.marketwatch.com/investing/stock/live').text
soup = BeautifulSoup(html_cont,'lxml')

stock = soup.find('tr',attrs = {'class':'table__row index is-active'})

# Name of the stoc
stock_name = stock.find('a',attrs = {'data-track-code':'MW_Header_Market Data_Quote Click_The Asia Dow Index USD'}).text

# Price of the stock
stock_price = stock.find('td',attrs = {'class':'table__cell change'}).text

#Percentage of Stock

# stock_percentage = stock.find('bg-quote',attrs = {'field':'percentchange'}).text

###################

stock_rate = stock.select('bg-quote.percentage')
print(stock_rate)