TODO
* obtain observations every few minutes
* obtain observations for all stocks in main market
* obtain observations for all stocks in leap and ace
* compute var
* compute volatility
* track sector performances
* allow building of portfolios
* realtime graph
* optimize data storage
* tracking at higher level
* recommend hedging positions
* introduce AI components
* recomend stocks that matches agrees with technical analysis
* obtain all the list where
* SCD type 2:changing of company index.
* Add time created to data gathering
* Obtain dividend and other company event data
* Introduce more table so it takes up less space.
   * dimension table


# malaysia_stock_analysis
Create program which download stock prices, processes, and recommends stocks to invest.

#Pre-requisite
- installed mysql
- created a schema called securities_master
  - for more information, checkout quantstart in the link below. The author gave a very good explanation on how to set up mysql, schema and create tables on mysql
-


#Set up mysql server to store stock price
#Send data and saw in sql
# to be able to retrieve data realtime
# to be able to retrieve data only when market is open
# retrieve all bursa stocks
# repeatly ping to obtain data




/******************************/
Mysql Portion
/****************************/
eg.
mysql -u root -p
create database securities_master;
use securities_master

sudo mysql
create database bursa_securities;
use bursa_securities;
CREATE USER 'bursa_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON bursa_securities.* TO 'bursa_user'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE `exchange` (
  `id` int NOT NULL AUTO_INCREMENT,
  `abbrev` varchar(32) NOT NULL,
  `name` varchar(255) NOT NULL,
  `city` varchar(255) NULL,
  `country` varchar(255) NULL,
  `currency` varchar(64) NULL,
  `timezone_offset` time NULL,
  `created_date` datetime NOT NULL,
  `last_updated_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

create table bursa_securities.fin_data5 (
                                         id int NOT NULL AUTO_INCREMENT,
                                         stock_code float,
                                         stock_name varchar(128),
                                         change_rm float,
                                         change_pct float,
                                         volume_hundred int,
                                         buy_vol int,
                                         buy_price float,
                                         sell_price float,
                                         sell_vol int,
                                         lacp float ,
                                         open float ,
                                         high float ,
                                         low float ,
                                         closed_price float,
                                         PRIMARY KEY (`id`)
                                         ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

* The scheduler need to be restart everytime the computer reboot.


* Question worth pondering?
** How do we account for company events in stock analysis? eg. share dividend, cash dividend, quarterly report, annual report.



















Appendix/Credits
* https://www.quantstart.com/articles/Securities-Master-Database-with-MySQL-and-Python/
* https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day
** pip install schedule /*install this*/
** eg. of python schedule
    import schedule
    import time

    def job(t):
        print "I'm working...", t
        return

    schedule.every().day.at("01:00").do(job,'It is 01:00')

    while True:
        schedule.run_pending()
        time.sleep(60) # wait one minute
** nohup python3 <python-script-to-run> &


*https://stackoverflow.com/questions/47086739/python-scheduling-a-job-starting-every-weekday-and-running-every-hour