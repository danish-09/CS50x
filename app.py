# flask has been used for the backend of the web application

from cs50 import SQL
from flask import Flask,render_template, redirect, request, session, redirect
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology


app = Flask(__name__)

# stores data on filesystem

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db=SQL("sqlite:///visitors.db")


@app.route("/")
@login_required
def home():
    return render_template("home.html")




@app.route("/places")
@login_required
def places():
    return render_template("places.html")




@app.route("/visit",methods=["GET","POST"])
@login_required
def visit():
    id=session["user_id"]
    if request.method=="POST":

        name=request.form.get("name")
        place=request.form.get("location")
        date=request.form.get("date")
        id_type=request.form.get("contacttype")
        contact=request.form.get("contact")

        db.execute("insert into people values(?,?,?,?,?,?)",id,name,place,date,id_type,contact)

        data=db.execute("select * from people where place=? and date=?",place,date)
        return render_template("visitors.html",data=data)

    else:
        return render_template("visit.html")




@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        username=request.form.get("username")
        if not username:
            return apology("username missing")

        password = request.form.get("password")
        if not password:
            return apology("password missing")

        rows=db.execute("select * from users1 where username=?",username)

        if len(rows) != 1 or not check_password_hash(rows[0]["passw"], request.form.get("password")):
            return apology("invalid username or password")

        session["user_id"]=rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")




@app.route("/logout")
@login_required
def logout():

    session.clear()
    return redirect("/")




@app.route("/register", methods=["GET", "POST"])
def register():

     if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("username missing")

        takenname = db.execute("select * from users1 where username=?", username)
        if len(takenname) != 0:
            return apology("username already taken")

        password = request.form.get("password")
        if not password:
            return apology("password missing")

        passw = generate_password_hash(password)
        db.execute("insert into users1(username,passw) values(?,?)",username,passw)
        return render_template("login.html")

     else:
         return render_template("register.html")




@app.route("/about")
def about():
    return render_template("about.html")

