import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

outF = open("myOutFile.txt", "w")
r = http.request('GET', 'https://www.bursamalaysia.com/trade/trading_resources/listing_directory/company-profile?stock_code=0096')
soupr=BeautifulSoup(r.data,'html.parser')
# print(r.data)
# sk=soupr.text
# soupr=soupr.prettify.text
# soupr=soupr.text

# with open("myOutFile.txt", 'w') as out_file:
#     r = http.request('GET', 'https://www.bursamalaysia.com/trade/trading_resources/listing_directory/company-profile?stock_code=0096')
#     soup = BeautifulSoup(r.data,'html.parser')
#     out_file.write(r)
# print(soupr)
# outF = open("myOutFile.txt", "w")
# for line in soupr:
#   print(<message>, file=<output_stream>)
# outF.close()

# a='fdsfsd'
with open('out.txt', 'w') as f:
    print(r.data, file=f)
