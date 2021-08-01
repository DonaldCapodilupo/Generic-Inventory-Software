from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def login_Screen():
    if request.method == 'POST':
        from backend import get_Current_User_Database_Information
        username = request.form['username']
        password = request.form['password']

        valid_Users = get_Current_User_Database_Information()

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
            from backend import add_Inventory_Item
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


            add_Inventory_Item(information_For_Inventory_DB)
            return render_template("add_Inventory.html" ,success=True, data=information_For_Inventory_DB)

        elif request.form['submit_button'] == 'Back To Main Menu':
            return redirect(url_for('main_Screen'))

    else:
        return render_template("add_Inventory.html")


@app.route('/Remove_Inventory_Item', methods=["POST","GET"])
def remove_Inventory_Item():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Go Back':
            return redirect(url_for('main_Screen'))

    else:
        return render_template("remove_Inventory_Item.html")

@app.route('/Send_Item_To_Job', methods=["POST","GET"])
def send_Item_To_Job():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Go Back':
            return redirect(url_for('main_Screen'))

    else:
        return render_template("send_Item_To_Job.html")


@app.route('/Return_Item_From_Job', methods=["POST","GET"])
def return_Item_From_Job():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Go Back':
            return redirect(url_for('main_Screen'))

    else:
        return render_template("return_Item_From_Job.html")


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


if __name__ == '__main__':
    from backend import programSetup
    programSetup()

    current_User = ""

    app.run()
