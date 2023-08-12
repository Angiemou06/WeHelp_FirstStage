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
def connect_to_database():
    try:
        con = mysql.connector.connect(
            user="root",
            password="123456",
            host="localhost",
            database="website"
        )
        cursor = con.cursor()
        return con, cursor
    except:
        return None, None
    
@app.route("/signup",methods=["POST"])
def signup():
    name = request.form["name"]
    account = request.form["account"]
    password = request.form["password"]
    con, cursor = connect_to_database()
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
    con, cursor = connect_to_database()
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
        id = session["id"]
        con, cursor = connect_to_database()
        cursor.execute("SELECT member.id,message.id,member.name,message.content FROM message INNER JOIN member ON message.member_id=member.id")
        result = cursor.fetchall()
        all_member_id = [row[0] for row in result]
        all_content_id=[row[1] for row in result]
        all_content_neme=[row[2] for row in result]
        all_content = [row[3] for row in result]
        con.commit()
        con.close()

        coefficient=[]
        for i in range(0,len(all_member_id)):
            if all_member_id[i] == id:
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
            con, cursor = connect_to_database()
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
    con, cursor = connect_to_database()
    cursor.execute("DELETE FROM message WHERE id=%s", (delete_message_id,))
    con.commit()
    con.close()
    return redirect("/member")

app.run(port=3000)