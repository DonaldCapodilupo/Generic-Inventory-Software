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
        pass

    else:
        return render_template("main.html")


if __name__ == '__main__':
    from backend import programSetup
    programSetup()
    app.run()
