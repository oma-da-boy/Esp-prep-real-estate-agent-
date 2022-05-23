import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plot


def login():
    """this function is responsible for login"""
    con = sql.connect("admin.db")
    curs = con.cursor()

    curs.execute("""CREATE TABLE IF NOT EXISTS admin_logins (username, password)""")
    curs.execute("SELECT * FROM admin_logins")
    db = curs.fetchall()

    count = 0
    while count < 3:
        username = input("username: ")
        password = input("password: ")

        for row in db:
            if row[0] == username and password == row[1]:
                print("login successful")
                menu()
            else:
                print("either username or password is incorrect,please try again")
        count = count + 1

    con.commit()
    con.close()


def menu():
    print(8 * "=", "welcome to Admin Panel ", 8 * "=")
    print(41 * "=")
    print("=  What would you like to do:")
    print('=  [1] <==================> sort through houses')
    print('=  [2] <==================> look at graphs')
    print(36 * "=")

    while True:
        choice = input("=  enter your choice here: ")

        if choice == "1":
            admin_sort()
        elif choice == "2":
            admin_graph()
        else:
            print("please select a valid option from the menu above, thank you.")


def admin_sort():
    """function sorts the items in the database"""
    while True:
        print(41 * "=")
        print("=  would you like to view the houses by:")
        print('=  [1] <==================> alphabetically')
        print('=  [2] <==================> by price')
        print('=  [3] <==================> by house type')
        print(36 * "=")
        choice = input("=  enter your choice here: ")

        con = sql.connect("house_prices.db")
        curs = con.cursor()

        # sorts the database based on user input
        if choice == "1":
            curs.execute("SELECT * FROM housePrices ORDER BY area")
            break
        elif choice == "2":
            curs.execute("SELECT * FROM housePrices ORDER BY price")
            break
        elif choice == "3":
            curs.execute("SELECT * FROM housePrices ORDER BY house_type")
            break
        else:
            print("please select a valid option from the menu above, thank you.")

    # prints out sorted list
    db = curs.fetchall()
    df = pd.DataFrame(db)
    df.columns = ["house id", "area", "house type", " number of bed", "price", "commission"]
    for row in df["price"]:
        txt = "£{money}"
        row = txt.format(money=row)
        df["price"] = row

    print(df)
    menu()


def admin_graph():
    """function makes graph based on user input"""
    while True:
        print(41 * "=")
        print("=  would you like to view graph showing:")
        print('=  [1] <==================> house types')
        print('=  [2] <==================> number of beds')
        print('=  [3] <==================> by area')
        print(36 * "=")
        choice = input("=  enter your choice here: ")

        con = sql.connect("house_prices.db")
        curs = con.cursor()


        # gets the values for the graph and sets labels
        if choice == "1":
            curs.execute("SELECT COUNT(area), house_type FROM housePrices GROUP BY house_type ")
            labelx = "house types"
            labely = "Available"
            break
        elif choice == "2":
            curs.execute("SELECT COUNT(area), bed_num FROM housePrices GROUP BY bed_num ")
            labelx = "number of beds"
            labely = "houses"
            break
        elif choice == "3":
            curs.execute("SELECT COUNT(house_type), area FROM housePrices GROUP BY area ")
            labelx = "houses"
            labely = "Available"
            break
        else:
            print("please select a valid option from the menu above, thank you.")

    x = []
    y = []

    db = curs.fetchall()
    for row in db:
        x.append(row[1])
        y.append(row[0])

    plot.figure(figsize=(10, 10))
    plot.bar(x, y)
    plot.ylabel(labely)
    plot.xlabel(labelx)
    plot.show()
    menu()