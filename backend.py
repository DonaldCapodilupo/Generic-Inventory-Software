
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
                                                  "Stock_ID TEXT)")
        except sqlite3.OperationalError:
            print("Inventory.db already exists.")




    create_User_Database()
    create_Tool_Database()

    os.chdir('..')