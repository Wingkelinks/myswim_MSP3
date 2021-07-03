import os
import re
from flask import (
    Flask, flash, render_template, 
    redirect, request,  session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from werkzeug.utils import escape
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# APP CONFIGURATION 

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME") ## DB NAME
app.config["MONGO_URI"] = os.environ.get("MONGO_URI") ## CONNECTION STRING
app.secret_key = os.environ.get("SECRET_KEY") ## SECRET KEY FOR FLASK FUNCTIONS

mongo = PyMongo(app) ## CREATE INSTANCE OF PYMONGO AND ADD FLASK APP OBJECT 

@app.route("/")
@app.route("/get_sets")
def get_sets():
    sets = mongo.db.sets.find()
    return render_template("sets.html", sets=sets)

# REGISTRATION 
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists within db
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists. Please try again.")
            return redirect(url_for("register"))
        
        # if no existing user is found create register dictionary
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Success! Welcome to MySwim.")
    return render_template("register.html")


# LOG IN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if username exists in db
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            #check hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    # put user into 'session' cookie
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome to MySwim {}!".format(request.form.get("username")))
            else:
                #invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


#PROFILE FUNCTIONALITY
@app.route("/profile<username>", methods=["GET","POST"])
def profile(username):
    # get session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True) ## UPDATE TO FALSE BEFORE DEPLOYMENT

