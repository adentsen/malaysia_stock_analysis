TODO
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
* to be able to retrieve data realtime
* to be able to retrieve data only when market is open
* retrieve all bursa stocks


# malaysia_stock_analysis
Create program which download stock prices, processes, and recommends stocks to invest.

SETUP
* Pre-requsite :
** set up mysql database
** python is installed with necessary libraries

* Procedure
** Clone repo to your local
** Modify the get_price parameters in scheduler.py
** Run the scheduler.py on your terminal
*** Scheduler.py need to be run everytime you reboot your computer

MYSQL details
* Table(s) needed:
** fin_data5

MYSQL DDL
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



EXTRA
* Code copied from quantstart
$ mysql -u root -p
mysql> CREATE DATABASE securities_master;
mysql> USE securities_master;
mysql> CREATE USER 'sec_user'@'localhost' IDENTIFIED BY 'password';
mysql> GRANT ALL PRIVILEGES ON securities_master.* TO 'sec_user'@'localhost';
mysql> FLUSH PRIVILEGES;

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

CREATE TABLE `data_vendor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `website_url` varchar(255) NULL,
  `support_email` varchar(255) NULL,
  `created_date` datetime NOT NULL,
  `last_updated_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `symbol` (
  `id` int NOT NULL AUTO_INCREMENT,
  `exchange_id` int NULL,
  `ticker` varchar(32) NOT NULL,
  `instrument` varchar(64) NOT NULL,
  `name` varchar(255) NULL,
  `sector` varchar(255) NULL,
  `currency` varchar(32) NULL,
  `created_date` datetime NOT NULL,
  `last_updated_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_exchange_id` (`exchange_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `daily_price` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data_vendor_id` int NOT NULL,
  `symbol_id` int NOT NULL,
  `price_date` datetime NOT NULL,
  `created_date` datetime NOT NULL,
  `last_updated_date` datetime NOT NULL,
  `open_price` decimal(19,4) NULL,
  `high_price` decimal(19,4) NULL,
  `low_price` decimal(19,4) NULL,
  `close_price` decimal(19,4) NULL,
  `adj_close_price` decimal(19,4) NULL,
  `volume` bigint NULL,
  PRIMARY KEY (`id`),
  KEY `index_data_vendor_id` (`data_vendor_id`),
  KEY `index_synbol_id` (`symbol_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
SQL


