
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


    create_User_Database()
    create_Tool_Database()

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


def add_Inventory_Item(user_Information_Tuple):
    import os
    import sqlite3
    os.chdir("Databases")



    conn = sqlite3.connect("Inventory.db")
    c = conn.cursor()
    c.execute("INSERT INTO Inventory VALUES (NULL,?,?,?,?,?,?,?)",user_Information_Tuple)
    os.chdir('..')
    conn.commit()