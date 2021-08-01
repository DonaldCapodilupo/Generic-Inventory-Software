
databases_To_Create = {
    "All Items":["tool","stock number", "available"],
    "Users":["username","password"]


}

def programSetup():
    import os
    import sqlite3
    try:
        os.mkdir("Databases")
        print("Database Directory Created ")
    except FileExistsError:
        print("Database directory already exists")

    os.chdir("Databases")

    def create_User_Database():
        conn = sqlite3.connect('Users.db')
        c = conn.cursor()
        try:
            c.execute("CREATE TABLE Userlist (ID INTEGER PRIMARY KEY, "
                                                  "Date TEXT, "
                                                  "Username TEXT,"
                                                  "Password TEXT)")
        except sqlite3.OperationalError:
            print("Users.db already exists.")

    def create_Tool_Database():
        conn = sqlite3.connect('Inventory.db')
        c = conn.cursor()
        try:
            c.execute("CREATE TABLE Inventory (ID INTEGER PRIMARY KEY, "
                      "Date TEXT, "
                      "Tool TEXT,"
                      "Tool_Type TEXT,"
                      "Stock_ID TEXT,"
                      "Cost TEXT,"
                      "Location TEXT,"
                      "User TEXT)")
        except sqlite3.OperationalError:
            print("Inventory.db already exists.")

    def create_Employee_Database():
        conn = sqlite3.connect('Employee.db')
        c = conn.cursor()
        try:
            c.execute("CREATE TABLE Employees (ID INTEGER PRIMARY KEY, "
                      "Stock_ID TEXT,"
                      "Date_Withdrawn TEXT, "
                      "Employee_Name TEXT,"
                      "Date_Returned TEXT)")
        except sqlite3.OperationalError:
            print("Employee.db already exists.")

    def create_Job_Database():
        conn = sqlite3.connect('Jobs.db')
        c = conn.cursor()
        try:
            c.execute("CREATE TABLE Jobs (ID INTEGER PRIMARY KEY, "
                      "Date TEXT,"
                      "Invoice_Number TEXT,"
                      "Client_Name TEXT, "
                      "Team_Leader TEXT)")
        except sqlite3.OperationalError:
            print("Employee.db already exists.")


    create_User_Database()
    create_Tool_Database()
    create_Employee_Database()
    create_Job_Database()
    os.chdir('..')


def get_Current_User_Database_Information():
    import os
    import sqlite3
    os.chdir("Databases")

    returnDict = {}

    conn = sqlite3.connect("Users.db")
    c = conn.cursor()
    for row in c.execute("SELECT * FROM Userlist ORDER BY Date"):
            returnDict[row[2]] = row[3]
    os.chdir('..')
    return  returnDict


def get_Current_Inventory_Database_Information():
    import os
    import sqlite3
    os.chdir("Databases")

    returnDict = {}

    conn = sqlite3.connect("Inventory.db")
    c = conn.cursor()
    for row in c.execute("SELECT * FROM Inventory ORDER BY Date"):
            returnDict[row[2]] = (row[1],row[4],row[7])
    os.chdir('..')
    return  returnDict


def add_Inventory_Item(user_Information_Tuple):
    import os
    import sqlite3
    os.chdir("Databases")



    conn = sqlite3.connect("Inventory.db")
    c = conn.cursor()
    c.execute("INSERT INTO Inventory VALUES (NULL,?,?,?,?,?,?,?)",user_Information_Tuple)
    os.chdir('..')
    conn.commit()


def remove_Inventory_Item(stock_ID):
    import os
    import sqlite3
    os.chdir("Databases")

    conn = sqlite3.connect("Inventory.db")
    c = conn.cursor()

    c.execute("DELETE FROM Inventory where Stock_ID = ?", [stock_ID])
    os.chdir('..')
    conn.commit()