# Purpose: Get stock information from Bursa website and save onto Mysql

# Import necessary packages
import datetime
import mysql.connector
import urllib3
from math import ceil
from bs4 import BeautifulSoup
from bs4 import re

def get_price( company_cd, in_tbl, db_host, db_user,db_password, db_database, auth_plugin = 'mysql_native_password'):
    # Obtain html script from Bursa and scrap data from the script
    http = urllib3.PoolManager()
    r    = http.request(
                    'GET', 'https://www.bursamalaysia.com/trade/trading_resources/listing_directory/company-profile?stock_code='+company_cd
                    )
    soup = BeautifulSoup(r.data, 'html.parser')
    # Get the company info and financial data
    stock_name = soup.title.text.split('(')[0]
    # Get the company stock data
    raw_data1      = soup.find_all(class_="m-0 table table-striped border-right border-grey")
    raw_data11     = raw_data1[0].text
    stock_code     = raw_data11.splitlines()[4].strip()
    change_rm      = raw_data11.splitlines()[9].strip()
    change_pct     = raw_data11.splitlines()[15].strip()
    volume_hundred = raw_data11.splitlines()[24].strip()
    volume_hundred = volume_hundred.replace(",", "")
    raw_data12     = raw_data1[1].text
    buy_vol        = raw_data12.splitlines()[4].strip()
    buy_vol        = buy_vol.replace(",", "")
    buy_price      = raw_data12.splitlines()[8].strip()
    sell_price     = raw_data12.splitlines()[12].strip()
    sell_vol       = raw_data12.splitlines()[16].strip()
    sell_vol       = sell_vol.replace(",", "")
    raw_data2      = soup.find_all(class_="m-0 table table-striped")
    raw_data21     = raw_data2[0].text
    lacp           = raw_data21.splitlines()[4].strip()
    open           = raw_data21.splitlines()[8].strip()
    high           = raw_data21.splitlines()[12].strip()
    low            = raw_data21.splitlines()[16].strip()
    raw_data3      = soup.find_all(class_="h5 bold mb-0")
    raw_data31     = raw_data3[0].text
    closed_price   = raw_data31.rstrip("/n")
    closed_price   = closed_price.strip()
    symbols        = []
    # Create a tuple (for the DB format) and append to the grand list
    symbols.append((stock_code,
                    stock_name,
                    change_rm,
                    change_pct,
                    volume_hundred,
                    buy_vol,
                    buy_price,
                    sell_price,
                    sell_vol,
                    lacp,
                    open,
                    high,
                    low,
                    closed_price))
    # Check the length of the tuple/list
    int_sy = list(j for i in symbols for j in i)
    c_sy = len(int_sy)
    # Convert any '-' to zero
    symbol_list = list(symbols[0])
    for i in range(c_sy):
        if symbol_list[i] == '-':
            symbol_list[i] = 0
    symbols = tuple(symbol_list)
    # Establish connection to mysql
    mydb = mysql.connector.connect(
                                    host        = db_host,
                                    user        = db_user,
                                    password    = db_password,
                                    database    = db_database,
                                    auth_plugin = 'mysql_native_password'
                                    )
    # Check if connection was successful
    if (mydb):
        # Carry out normal procedure
        print("Connection successful")
    else:
        # Terminate
        print("Connection unsuccessful")
    # Create the insert strings
    column_str = "stock_code, stock_name, change_rm, change_pct,volume_hundred,buy_vol,buy_price,sell_price,sell_vol,lacp,open,high,low,closed_price"
    insert_str = ("%s, " * 14)[:-2]
    final_str  = "INSERT INTO "+ in_tbl+ "(%s) VALUES (%s)" % (column_str, insert_str)
    val        = symbols
    # Insert data to db
    cur = mydb.cursor()
    cur.execute(final_str, val)
    mydb.commit()
