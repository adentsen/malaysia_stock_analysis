# Purpose: Enable get_price to run only during business hours

import time
import datetime
import schedule
from download_stock_price_from_bursa import get_price

# get_price(company_cd  = "0002",
#                 in_tbl      = "fin_data5",
#                 db_host     = "localhost",
#                 db_user     = "bursa_user",
#                 db_password = "password",
#                 db_database = "bursa_securities",
#                 )


# Only run get price if it is a weekday from 9 to 5
def main():
  dttm = datetime.datetime.now()
  weekno = datetime.datetime.today().weekday()
  at9am = dttm.replace(hour=9, minute=0, second=0, microsecond=0)
  at5pm = dttm.replace(hour=17, minute=0, second=0, microsecond=0)
  if weekno<5:
    if dttm > at9am and dttm < at5pm:
      get_price(company_cd  = "0002",
                in_tbl      = "fin_data5",
                db_host     = "localhost",
                db_user     = "bursa_user",
                db_password = "password",
                db_database = "bursa_securities",
                )

schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)

