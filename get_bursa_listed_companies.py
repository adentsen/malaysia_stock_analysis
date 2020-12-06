# Purpose: To obtain Bursa listed companies

# Import necessary packages
import urllib3

import datetime
from bs4 import BeautifulSoup
import os

fname="my_companies_"+str(datetime.datetime.now().date())+".txt"

if os.path.exists(fname):
   # append if already exists
   append_write = 'a'
else:
   # make a new file if not
   append_write = 'w'

doc = open(fname,append_write)
doc.close()

# Test webpage, if able to run get request then output the name of the companies and index
for x in range(5):
   try:
      pg=http.request('GET', 'https://www.bursamalaysia.com/trade/trading_resources/listing_directory/company-profile?stock_code='+str(x).zfill(4))
   except:
      print ("This index has not been assigned yet: "+ str(x) )
   else:
      # Get the company info and financial data
      soup = BeautifulSoup(pg.data, 'html.parser')
      stock_name = soup.title.text.split('(')[0]
      with open(fname, 'a') as f:
         print(str(x).zfill(4)+" "+ stock_name,file=f)





