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
def signin():
    name = request.form["account_signin"]
    password = request.form["password_signin"]
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor=con.cursor()
    cursor.execute("SELECT id,name,username FROM member WHERE username=%s AND password=%s",(name,password))
    result = cursor.fetchone()
    con.close()
    if result:
        session["id"] = result[0]
        session["user"] =result[1]
        session["username"]=result[2]
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
        id = session["id"]
        con = mysql.connector.connect(
            user="root",
            password="123456",
            host="localhost",
            database="website"
        )
        cursor = con.cursor()
        cursor.execute("SELECT message.content FROM message INNER JOIN member ON message.member_id=member.id WHERE message.member_id=%s",(id,))
        result = cursor.fetchall()
        signin_member_content=[row[0] for row in result]

        cursor.execute("SELECT message.id,member.name,message.content FROM message INNER JOIN member ON message.member_id=member.id")
        result = cursor.fetchall()
        all_content_id=[row[0] for row in result]
        all_content_neme=[row[1] for row in result]
        all_content = [row[2] for row in result]
        con.commit()
        con.close()

        coefficient=[]
        for text in all_content:
            if text in signin_member_content:
                coefficient.append(1)
            else:
                coefficient.append(0)
        
        return render_template("member.html" ,us_name=name, all_content_neme=all_content_neme, all_content=all_content, all_content_id=all_content_id, coefficient=coefficient)
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
    delete_message_id = request.form["delete_message_id"]
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor = con.cursor()
    cursor.execute("DELETE FROM message WHERE id=%s", (delete_message_id,))
    con.commit()
    con.close()
    return redirect("/member")

app.run(port=3000)