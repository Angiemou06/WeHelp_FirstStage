from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
import mysql.connector

app = Flask(__name__)
app.secret_key = "It's a secret!"
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/signup",methods=["POST"])
def signup():
    name = request.form["name"]
    account = request.form["account"]
    password = request.form["password"]
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor = con.cursor()
    cursor.execute("SELECT id FROM member WHERE username = %s", (account,))
    existing_user = cursor.fetchone()
    if existing_user is not None:
        con.close()
        return redirect("/error?message=帳號已被註冊")      
    else:
        cursor.execute("INSERT INTO member(name,username,password) VALUES (%s,%s,%s)",(name, account, password))
        con.commit()
        con.close()
        session["user"] = name
        return redirect("/")

@app.route("/signin", methods=["POST"])
def login():
    name = request.form["user"]
    password = request.form["password"]
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor=con.cursor()
    cursor.execute("SELECT * from member")
    data=cursor.fetchall()
    data_id=[]
    data_name=[]
    data_username=[]
    data_password=[]
    for text in data:
        data_id.append(text[0])
        data_name.append(text[1])
        data_username.append(text[2])
        data_password.append(text[3])
    con.commit()
    con.close()
    for i in range(0,len(data_username)):
        if (name == data_username[i] and password == data_password[i]):
            session["id"] = data_id[i]
            session["user"] = data_name[i]
            session["username"] = data_username[i]
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
        name = session["user"]
        username = session["username"]
        con = mysql.connector.connect(
            user="root",
            password="123456",
            host="localhost",
            database="website"
        )
        cursor = con.cursor()
        cursor.execute("SELECT id,member_id,content FROM message")
        result = cursor.fetchall()
        message_id=[row[0] for row in result]
        content = [row[2] for row in result]
        member_id = [row[1] for row in result]

        cursor.execute("SELECT id FROM member WHERE username=%s",(username,))
        id = cursor.fetchone()[0]
        data_number = len(content)
        coefficient = [0] * data_number
        for i in range(0,data_number):
            if member_id[i] == id:
                coefficient[i] = 1

        message_name_list=[]
        for i in member_id:
            cursor.execute("SELECT name FROM member WHERE id=%s",(i,))
            message_name =  cursor.fetchone()[0]
            message_name_list.append(message_name)
        con.commit()
        con.close()
        return render_template("member.html" ,us_name=name, message_id=message_id, content=content, message_name=message_name_list, coefficient=coefficient)
    else:
        return redirect("/")
    
@app.route("/createMessage", methods=["POST"])
def createMessage():
    id = session["id"]
    if request.method == "POST":
        text = request.form["message"]
        if text:
            con = mysql.connector.connect(
                user="root",
                password="123456",
                host="localhost",
                database="website"
            )
            cursor=con.cursor()
            cursor.execute("INSERT INTO message(member_id,content) VALUES (%s,%s)",(id, text))
            con.commit()
            con.close()
    return redirect("/member")

@app.route("/signout")
def signout():
    del session["id"]
    del session["user"]
    del session["username"]
    return redirect("/")

@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    message_id = request.form["message_id"]
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor = con.cursor()
    cursor.execute("DELETE FROM message WHERE id=%s", (message_id,))
    con.commit()
    con.close()
    return redirect("/member")

app.run(port=3000)