import time
from datetime import datetime

def job(message='stuff'):
   now = datetime.now()
   print("I'm working on:", message + "The time is " + str(now))


schedule.every(5).minutes.do(job)
# schedule.every().day.at("10:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)