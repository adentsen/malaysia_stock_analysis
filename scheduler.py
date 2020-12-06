# Purpose: Enable get_price to run only during business hours

import time
from datetime import datetime
import schedule
from download_stock_price_from_bursa import get_price

# Only run get price if it is a weekday from 9 to 5
def main():
  dttm = datetime.datetime.now()
  weekno = datetime.datetime.today().weekday()
  if weekno<5:
    if dttm.time() >= 9 and dttm.time() <=5:
      get_price(company_cd  = "7106",
                in_tbl      = "fin_data5",
                db_host     = "localhost",
                db_user     = "bursa_user",
                db_password = "password",
                db_database = "bursa_securities",
                )

schedule.every(10).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)