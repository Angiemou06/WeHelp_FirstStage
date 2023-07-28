from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session

app = Flask(__name__)
app.secret_key = "It's a secret!"
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/signin", methods=["POST"])
def login():
    name = request.form["user"]
    password = request.form["password"]
    confirm = request.form.get("confirm")
    if (name == "" or  password == ""):
        return redirect("/error")
    elif (name == "test" and password == "test"):
        session["user"] = name
        return redirect("/member")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

@app.route("/error")
def error():
    error_msg = request.args.get("message")
    return render_template("error.html", error_msg=error_msg)

@app.route("/member")
def member():
    if "user" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/signout")
def signout():
    del session["user"]
    return redirect("/")

@app.route("/square/<int:number>")
def square(number):
    if number > 0:
        result = number * number
        return render_template("square.html", data=result)
    
app.run(port=3000)