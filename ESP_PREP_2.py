import ESP_PREP_3 as admin
import sqlite3 as sql
import pandas as pd
import time


# noinspection PyBroadException
def customer():
    # declare global variables
    area = ""
    beds = ""
    budget = 0

    # getting area
    print(8 * "=", "welcome to House Hunter", 8 * "=")
    print(41 * "=")
    print("=  Select a area you are interested in")
    print('=  [1] <==================> Manchester')
    print('=  [2] <==================> York')
    print('=  [3] <==================> Liverpool')
    print('=  [4] <==================> Newcastle')
    print('=  [5] <==================> Birmingham')
    print('=  [6] <==================> Oldham')
    print('=  [7] <==================> Bury')
    print('=  [8] <==================> Rochdale')
    print('=  [9] <==================> Salford')
    print(36 * "=")
    areas = ['Manchester', 'York', 'Liverpool', 'Newcastle', 'Birmingham', 'Oldham', 'Bury', 'Rochdale', 'Salford']
    index = input("=  enter your choice here: ")

    try:
        int(index)
    except:
        print("please select a valid *number* option from the menu above, thank you.")

    index = int(index)
    if 0 < index < 10:
        area = areas[index - 1]
    else:
        print("please select a valid option from the menu above, thank you.")

    # getting budget
    print(36 * "=")
    print("=  Select a budget from below")
    print('=  [1] <==================> 100,000')
    print('=  [2] <==================> 200,000')
    print('=  [3] <==================> 300,000')
    print('=  [4] <==================> 400,000')
    print('=  [5] <==================> 500,000')
    print(36 * "=")
    prices = ['100,000', '200,000', '300,000', '400,000', '500,000']
    index = input("=  enter your choice here: ")

    try:
        int(index)
    except:
        print("please select a valid *number* option from the menu above, thank you.")

    index = int(index)
    if 0 < index < 6:
        budget = prices[index - 1]
    else:
        print("please select a valid option from the menu above, thank you.")

    # getting number of beds
    print(36 * "=")
    print("=  How many beds would you like?")
    print('=  [1] <==================> One')
    print('=  [2] <==================> Two')
    print('=  [3] <==================> Three')
    print('=  [4] <==================> Four')

    print(36 * "=")
    bed = [1, 2, 3, 4]
    index = input("=  enter your choice here: ")

    try:
        int(index)
    except:
        print("please select a valid *number* option from the menu above, thank you.")

    index = int(index)
    if 0 < index < 5:
        beds = bed[index - 1]
    else:
        print("please select a valid option from the menu above, thank you.")
    print("gathering options: ")
    time.sleep(1)

    # gets the results based on user input
    con = sql.connect("house_prices.db")
    curs = con.cursor()
    curs.execute(
        "SELECT house_id, price, price * (deposit_percent / 100.0) FROM housePrices WHERE area = '{}' AND bed_num = '{}' AND price < '{}'".format(
            area, beds, budget))
    db = curs.fetchall()

    if bool(db):
        df = pd.DataFrame(db)
        df.columns = ["house id", "price", "commission"]
        for row in df["commission"]:
            txt = "£{money}"
            row = txt.format(money=row)
            df["commission"] = row
        for row in df["price"]:
            txt = "£{money}"
            row = txt.format(money=row)
            df["price"] = row
        print(df)
    else:
        print("No houses match your query")

    con.commit()
    con.close()
    time.sleep(5)


while True:
    print(8 * "=", "welcome to House Hunter", 8 * "=")
    print(41 * "=")
    print("=  please select which you are")
    print('=  [1] <==================> Staff')
    print('=  [2] <==================> Customer')
    ans = input("=  enter choice here:")

    if ans == "1":
        admin.login()
    elif ans == "2":
        customer()
    else:
        print("please select a valid option from the menu above, thank you.")
