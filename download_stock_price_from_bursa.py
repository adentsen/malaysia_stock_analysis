
import urllib3

from math import ceil

from bs4 import BeautifulSoup
from bs4 import re


http = urllib3.PoolManager()
r = http.request('GET', 'https://www.bursamalaysia.com/trade/trading_resources/listing_directory/company-profile?stock_code=5398')

#Process html file so we can use BeutifulSoup method on it
soup=BeautifulSoup(r.data,'html.parser')
# print (soup)

# Get the company info and financial data 
stock_name=soup.title.text.split('(')[0] 

raw_data1=soup.find_all(class_="m-0 table table-striped border-right border-grey")
raw_data11=raw_data1[0].text
stock_code=raw_data11.splitlines()[4].strip()
change_rm=raw_data11.splitlines()[9].strip()
change_pct=raw_data11.splitlines()[15].strip()
volume_hundred=raw_data11.splitlines()[24].strip()
volume_hundred=volume_hundred.replace(",","")


raw_data12=raw_data1[1].text
buy_vol=raw_data12.splitlines()[4].strip()
buy_vol=buy_vol.replace(",","")
buy_price=raw_data12.splitlines()[8].strip()
sell_price=raw_data12.splitlines()[12].strip()
sell_vol=raw_data12.splitlines()[16].strip()
sell_vol=sell_vol.replace(",","")

raw_data2=soup.find_all(class_="m-0 table table-striped")
raw_data21=raw_data2[0].text

lacp=raw_data21.splitlines()[4].strip()
open=raw_data21.splitlines()[8].strip()
high=raw_data21.splitlines()[12].strip()
low=raw_data21.splitlines()[16].strip()

symbols = []
 # Create a tuple (for the DB format) and append to the grand list
symbols.append( (stock_code,stock_name,change_rm,change_pct,volume_hundred,buy_vol,buy_price,sell_price,sell_vol,lacp,open,high,low))
#   return symbols

import mysql.connector

mydb = mysql.connector.connect(
       host="localhost",
       user="bursa_user",
       password="password",
       database="bursa_securities",
       auth_plugin='mysql_native_password'
       )

# Check if connection was successful
if (mydb):
  # Carry out normal procedure
  print ("Connection successful")
else:
  # Terminate
  print ("Connection unsuccessful")


# Create the insert strings
column_str = "stock_code,stock_name,change_rm,change_pct,volume_hundred,buy_vol,buy_price,sell_price,sell_vol,lacp,open,high,low"
# insert_str = 
insert_str = ("%s, " * 13)[:-2]
final_str = "INSERT INTO fin_data4 (%s) VALUES (%s)" % (column_str, insert_str)
val=tuple(symbols[0])
# print (final_str, val)
print(insert_str)

cur = mydb.cursor()
cur.execute(final_str, val)

mydb.commit()


# # Using the MySQL connection, carry out an INSERT INTO for every symbol
# with mydb: 
#   cur = mydb.cursor()
#   # This line avoids the MySQL MAX_PACKET_SIZE
#   # Although of course it could be set larger!
#   for i in range(0, int(ceil(len(symbols) / 100.0))):
#     cur.executemany(final_str, symbols[i*100:(i+1)*100-1])

# for i in range(0, int(ceil(len(symbols) / 100.0))):
#   cur.executemany(final_str, symbols[i*100:(i+1)*100-1])
