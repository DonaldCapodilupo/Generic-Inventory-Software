from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def login_Screen():
    if request.method == 'POST':
        from backend import read_Database
        username = request.form['username']
        password = request.form['password']

        users_DB = read_Database("Users.db", "Userlist")



        valid_Users = dict(zip(users_DB["Username"],users_DB["Password"]))

        for user, pwrd in valid_Users.items():
            if user == username and password == pwrd:
                return redirect(url_for("main_Screen"))
        return render_template("login.html" ,error = True)


    else:
        return render_template("login.html")

@app.route('/main', methods=["POST","GET"])
def main_Screen():
    if request.method == 'POST':
        print(request.form)
        if request.form['submit_button'] == 'Add Inventory Item':
            return redirect(url_for('add_Inventory_Item'))
        elif request.form['submit_button'] == 'Remove Inventory Item':
            return redirect(url_for('remove_Inventory_Item'))
        elif request.form['submit_button'] == 'Send Item To Job':
            return redirect(url_for('send_Item_To_Job'))
        elif request.form['submit_button'] == 'Return Item From Job':
            return redirect(url_for('return_Item_From_Job'))
        elif request.form['submit_button'] == 'Get Reports':
            return redirect(url_for('view_Reports'))
        elif request.form['submit_button'] == 'View Letters':
            return redirect(url_for('view_Letters'))

    else:
        return render_template("main.html")

@app.route('/Add_Inventory_Item', methods=["POST","GET"])
def add_Inventory_Item():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Add Item':
            from backend import create_Database_Row
            import datetime
            today = str(datetime.date.today())
            information_For_Inventory_DB = (today,request.form['tool_Name'], request.form['Tools'],
                                            request.form['stock_Id'], request.form['cost'], request.form['location'],
                                            "Dcapodilupo")
            for user_Input in information_For_Inventory_DB:
                if user_Input:
                    pass
                else:
                    return render_template("add_Inventory.html", error=True, data=information_For_Inventory_DB)
            create_Database_Row("Inventory.db","Inventory",information_For_Inventory_DB)
            create_Database_Row("Backup_Inventory.db", "Inventory", information_For_Inventory_DB)

            return render_template("add_Inventory.html" ,success=True, data=information_For_Inventory_DB)
        elif request.form['submit_button'] == 'Back To Main Menu':
            return redirect(url_for('main_Screen'))
    else:
        return render_template("add_Inventory.html")

@app.route('/Remove_Inventory_Item', methods=["POST","GET"])
def remove_Inventory_Item():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Remove Item':
            from backend import delete_Database_Row, read_Database

            if request.form.getlist('checkbox'):
                for item in  request.form.getlist('checkbox'):
                    delete_Database_Row("Inventory.db","Inventory",item)

                    inv_Data = read_Database("Inventory.db", "Inventory")

                    records = inv_Data.to_records(index=False)
                    result = list(records)
                    print(result)
                    data_Zip = dict(zip(inv_Data["Tool"], result))

                return render_template("remove_Inventory_Item.html" ,inventory_Data=data_Zip,
                                       success=True, data= request.form.getlist('checkbox'))
            else:
                inv_Data = read_Database("Inventory.db", "Inventory")

                records = inv_Data.to_records(index=False)
                result = list(records)

                data_Zip = dict(zip(inv_Data["Tool"], result))
                return render_template("remove_Inventory_Item.html",
                                       inventory_Data=data_Zip,
                                       error=True)

        elif request.form['submit_button'] == 'Go Back':
            return redirect(url_for('main_Screen'))

    else:
        from backend import read_Database

        inv_Data = read_Database("Inventory.db","Inventory")

        records = inv_Data.to_records(index=False)
        result = list(records)

        data_Zip = dict(zip(inv_Data["Tool"],result))

        return render_template("remove_Inventory_Item.html",inventory_Data=data_Zip)

@app.route('/Send_Item_To_Job', methods=["POST","GET"])
def send_Item_To_Job():
    from backend import read_Database, create_Database_Row, delete_Database_Row
    if request.method == 'POST':
        if request.form['submit_button'] == 'Send Tool To Job':
            import datetime
            today = str(datetime.date.today())

            user_Input = {"invoice_Radio_Buttons":request.form['invoice_Radio_Buttons'],
                          "invoice_Number":"",
                          "contractor_Name":"",
                          "employee_Name":request.form['employee_Name'],
                          "tool_ID":request.form['tool_ID']
                          }

            if user_Input["invoice_Radio_Buttons"] == "New Invoice":

                user_Input["invoice_Number"] = request.form['invoice_Number_New']

                if request.form["invoice_Radio_Button_Contractor"] == "Previous Contractor":
                    user_Input["contractor_Name"] = request.form['contractor_Name_Previous']
                else:
                    user_Input["contractor_Name"] = request.form['contractor_Name_New']

                job_Information_Tuple = (today, user_Input["invoice_Number"], user_Input["contractor_Name"])

                create_Database_Row("Jobs.db", "Jobs",job_Information_Tuple)




            else:
                previous_Invoice_Information = request.form['invoice_Number'].split('|')
                user_Input["invoice_Number"] = previous_Invoice_Information[0]
                user_Input["contractor_Name"] = previous_Invoice_Information[1]


            outstanding_Tool_Information_Tuple = (today, user_Input["invoice_Number"], user_Input["contractor_Name"],
                                      user_Input["tool_ID"], user_Input["employee_Name"], False)

            create_Database_Row("Outstanding_Tools.db","Outstanding_Tools", outstanding_Tool_Information_Tuple)


            delete_Database_Row("Inventory.db","Inventory",user_Input["tool_ID"])

            return redirect(url_for('main_Screen'))


        else:
            pass
    else:

        inventory_DB = read_Database("Inventory.db","Inventory")
        jobs_DB = read_Database("Jobs.db", "Jobs")
        employees_DB = read_Database("Employee.db", "Employees")


        inventory_Info_Dict = dict(zip(inventory_DB["Tool"],inventory_DB["Stock_ID"]))

        employee_Name_List = employees_DB["Employee_Name"]

        invoice_Data_Dict = dict(zip(jobs_DB["Invoice_Number"],jobs_DB["Client_Name"]))

        contractor_Name_List = jobs_DB["Client_Name"]



        return render_template("send_Item_To_Job.html",
                               inventory_Data=inventory_Info_Dict,
                               employee_Data= employee_Name_List,
                               invoice_Data=invoice_Data_Dict ,
                               contractor_Data = contractor_Name_List)


@app.route('/Return_Item_From_Job', methods=["POST","GET"])
def return_Item_From_Job():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Go Back':
            return redirect(url_for('main_Screen'))
        if request.form['submit_button'] == 'Return Item From Job':
            from backend import delete_Database_Row, read_Database, create_Database_Row
            items_To_Return_To_Inventory = request.form.getlist('id_Checkboxes')

            backup_Dataframe = read_Database("Backup_Inventory.db", "Inventory")




            cat = backup_Dataframe.loc[backup_Dataframe['Stock_ID'] == items_To_Return_To_Inventory[0]]
            print(cat.values)
            print(cat.Stock_ID)



            for tool_Returned in items_To_Return_To_Inventory:
                delete_Database_Row("Outstanding_Tools.db","Outstanding_Tools", tool_Returned)

                backup_Information = backup_Dataframe.loc[backup_Dataframe['Stock_ID'] ==tool_Returned]
                print(backup_Information)
                create_Database_Row("Inventory.db","Inventory", backup_Information.values[0][1:])


            return redirect(url_for('main_Screen'))



    else:
        from backend import read_Database
        outstanding_Tools = read_Database("Outstanding_Tools.db", "Outstanding_Tools")

        #main_Divs = dict(zip(outstanding_Tools["Invoice_Number"],outstanding_Tools["Client_Name"]))

        invoice_Information = {}

        for row in outstanding_Tools.values:
            try:
                invoice_Information[row[2]].append((row[3], row[5], row[4], row[1]))
            except KeyError:
                invoice_Information[row[2]] = [(row[3], row[5], row[4], row[1])]

        print(invoice_Information)

        return render_template("return_Item_From_Job.html",
                               outstanding_Tools=invoice_Information,)


@app.route('/View_Reports', methods=["POST","GET"])
def view_Reports():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Go Back':
            return redirect(url_for('main_Screen'))

    else:
        return render_template("view_Reports.html")


@app.route('/View_Letters', methods=["POST","GET"])
def view_Letters():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Go Back':
            return redirect(url_for('main_Screen'))

    else:
        return render_template("view_Letters.html")

from backend import programSetup
programSetup()

if __name__ == '__main__':


    current_User = ""

    app.run()
