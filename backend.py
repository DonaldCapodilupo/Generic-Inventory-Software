
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
                      "Stock_ID TEXT,"
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

    def create_Backup_Database():
        conn = sqlite3.connect('Backup_Inventory.db')
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
            print("Backup_Inventory.db already exists.")


    create_User_Database()
    create_Tool_Database()
    create_Employee_Database()
    create_Job_Database()
    create_Outstanding_Tools_Database()
    create_Backup_Database()
    os.chdir('..')

def create_Database_Row(database, table, tuple_Of_Values_To_Add):
    import os
    import sqlite3
    os.chdir("Databases")

    conn = sqlite3.connect(database)
    c = conn.cursor()

    tuple_To_Database_Syntax = "?, " * (len(tuple_Of_Values_To_Add)-1)

    c.execute("INSERT INTO "+table+" VALUES (NULL,"+tuple_To_Database_Syntax +"?)",tuple_Of_Values_To_Add)
    os.chdir('..')
    conn.commit()

def read_Database(database, table):
    import pandas as pd
    import sqlite3, os

    os.chdir("Databases")

    con = sqlite3.connect(database)
    df = pd.read_sql_query("SELECT * from "+ table, con)
    con.close()
    os.chdir("..")
    return df

def update_Database_Information():
    pass

def delete_Database_Row(database, table, value_To_Remove):
    import os
    import sqlite3
    os.chdir("Databases")

    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("DELETE FROM "+ table +" where Stock_ID = ?", [value_To_Remove])
    os.chdir('..')
    conn.commit()


def get_Backup_Inventory_Item_Based_On_Stock_ID(dataframe, stock_ID):

    pass


