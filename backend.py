
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

    def create_Outstanding_Tools_Database():
        conn = sqlite3.connect('Outstanding_Tools.db')
        c = conn.cursor()
        try:
            c.execute("CREATE TABLE Outstanding_Tools (ID INTEGER PRIMARY KEY, "
                      "Date TEXT,"
                      "Invoice_Number TEXT,"
                      "Client_Name TEXT,"
                      "Tool_ID TEXT,"
                      "Employee TEXT,"
                      "Returned BOOLEAN)")
        except sqlite3.OperationalError:
            print("Outstanding_Tools.db already exists.")

    def create_Employee_Database():
        conn = sqlite3.connect('Employee.db')
        c = conn.cursor()
        try:
            c.execute("CREATE TABLE Employees (ID INTEGER PRIMARY KEY, "
                      "Employee_Name TEXT)")
        except sqlite3.OperationalError:
            print("Employee.db already exists.")

    def create_Job_Database():
        conn = sqlite3.connect('Jobs.db')
        c = conn.cursor()
        try:
            c.execute("CREATE TABLE Jobs (ID INTEGER PRIMARY KEY, "
                      "Date TEXT,"
                      "Invoice_Number TEXT,"
                      "Client_Name TEXT)")
        except sqlite3.OperationalError:
            print("Jobs.db already exists.")


    create_User_Database()
    create_Tool_Database()
    create_Employee_Database()
    create_Job_Database()
    create_Outstanding_Tools_Database()
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


def get_Current_Employee_Database_Information():
    import os
    import sqlite3
    os.chdir("Databases")

    returnList = []

    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()
    for row in c.execute("SELECT * FROM Employees ORDER BY ID"):
            returnList.append(row[1])
    os.chdir('..')
    return  returnList

def get_Current_Contractor_Database_Information():
    import os
    import sqlite3
    os.chdir("Databases")

    returnList = []

    conn = sqlite3.connect("Jobs.db")
    c = conn.cursor()
    for row in c.execute("SELECT * FROM Jobs ORDER BY ID"):
        if row[3]not in returnList:
            returnList.append(row[3])
    os.chdir('..')
    return  returnList

def get_Current_Invoice_Database_Information():
    import os
    import sqlite3
    os.chdir("Databases")

    returnList = []

    conn = sqlite3.connect("Jobs.db")
    c = conn.cursor()
    for row in c.execute("SELECT * FROM Jobs ORDER BY ID"):
        if row[3]not in returnList:
            returnList.append(row[3])
    os.chdir('..')
    return  returnList


def database_Retrieval_Tool(database, table_Name, desired_ReturnValues, allow_Duplicates=True):
    import sqlite3
    import os

    os.chdir("Databases")

    connection_To_Database = sqlite3.connect(database)
    cursor_For_Table = connection_To_Database.cursor()


    cursor_For_Table.execute(("PRAGMA table_info("+table_Name+")"))
    column_Headers = [headers[1] for headers in cursor_For_Table.fetchall()]

    desired_Column = column_Headers.index(desired_ReturnValues)

    return_List = [row[desired_Column] for row in
                   cursor_For_Table.execute("SELECT * FROM " + table_Name + " ORDER BY ID")]

    if allow_Duplicates:
        os.chdir("..")
        return return_List

    else:
        return_List_No_Duplicates = []
        [return_List_No_Duplicates.append(item) for item in return_List if item not in return_List_No_Duplicates]
        os.chdir("..")
        return return_List_No_Duplicates



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


def add_New_Job_Item(job_Information_Tuple):
    import os
    import sqlite3
    os.chdir("Databases")



    conn = sqlite3.connect("Jobs.db")
    c = conn.cursor()
    c.execute("INSERT INTO Jobs VALUES (NULL,?,?,?)",job_Information_Tuple)
    os.chdir('..')
    conn.commit()


def add_Outstanding_Tools_DB(job_Information_Tuple):
    import os
    import sqlite3
    os.chdir("Databases")

    conn = sqlite3.connect("Outstanding_Tools.db")
    c = conn.cursor()
    c.execute("INSERT INTO Outstanding_Tools VALUES (NULL,?,?,?,?,?,?)",job_Information_Tuple)
    os.chdir('..')
    conn.commit()