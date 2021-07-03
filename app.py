import os
import re
from flask import (
    Flask, flash, render_template, 
    redirect, request,  session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True) ## UPDATE TO FALSE BEFORE DEPLOYMENT

