import csv
import sqlite3 as sql
# this code moves all values from the csv file to a database

# opens csv
temp = open("house_prices.csv")
temp = csv.reader(temp)

# connects/creates to the database
con = sql.connect("house_prices.db")
curs = con.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS housePrices (house_id, area, house_type, bed_num, price, deposit_percent) """)
curs.execute("SELECT * FROM housePrices")

# moves the values from csv to db

count = 0
for row in temp:
    if count > 0:
        curs.execute("INSERT INTO housePrices VALUES (?, ?, ?, ?, ?, ?)", row)
    count = 1

con.commit()
con.close()
