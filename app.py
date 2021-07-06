import os
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

# GET SETS PAGE
@app.route("/")
@app.route("/get_sets")
def get_sets():
    sets = list(mongo.db.sets.find()) # wrap 'find' method inside python list
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


# LOG IN FUNCTIONALITY
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome to MySwim, {}!".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


#PROFILE FUNCTIONALITY
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    sets = list(mongo.db.sets.find(
        {"created_by": session["user"]}).sort("_id", 1))
    categories = list(mongo.db.categories.find())

    if session["user"]:
        return render_template("profile.html", username=username, sets=sets, categories=categories)

    return redirect(url_for("login"))


#LOG OUT FUNCTIONALITY
@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    #session.pop specifically removes user cookie
    session.pop("user")
    return redirect(url_for("login"))


# ADD NEW SWIM SET
@app.route("/add_set", methods=["GET", "POST"])
def add_set():
    if request.method == "POST":
        set = {
            "category_name": request.form.get("category_name"),
            "set_name": request.form.get("set_name"),
            "warm_up": request.form.get("warm_up"),
            "pre_set": request.form.getlist("pre_set"),
            "main_set": request.form.getlist("main_set"),
            "cool_down": request.form.get("cool_down"),
            "total_km": request.form.get("total_km"),
            "created_by": session["user"]
        }
        mongo.db.sets.insert_one(set)
        flash("Sucess! Your set has been added.")
        return redirect(url_for("get_sets"))
    #find categories in db and sort a-z
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_set.html", categories=categories)


# EDIT SWIM SET
@app.route("/edit_set/<set_id>", methods=["GET", "POST"])
def edit_set(set_id):
    if request.method == "POST":
        edit = {
            "category_name": request.form.get("category_name"),
            "set_name": request.form.get("set_name"),
            "warm_up": request.form.get("warm_up"),
            "pre_set": request.form.getlist("pre_set"),
            "main_set": request.form.getlist("main_set"),
            "cool_down": request.form.get("cool_down"),
            "total_km": request.form.get("total_km"),
            "created_by": session["user"]
        }
        mongo.db.sets.update({"_id": ObjectId(set_id)}, edit)
        flash("Sucess! Your set has been updated.")   

    set = mongo.db.sets.find_one({"_id": ObjectId(set_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_set.html", set=set, categories=categories)




# VIEW SETS IN USER PROFILE
@app.route("/view_set/<set_id>")
def view_set(set_id):
    set = mongo.db.sets.find_one({"_id": ObjectId(set_id)})
    user = mongo.db.users.find_one({"username": set["created_by"]})
    categories = list(mongo.db.categories.find())

    return render_template("view_set.html", set=set,
                           categories=categories, user=user)



# FAVOURITE AND ADD SET TO USER PROFILE 


# GET CATEGORIES FOR MANAGE CONTENT PAGE BY ADMIN
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("manage_content.html", categories=categories)

# ADD CATEGORY FUNCTION FOR ADMIN
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_content.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True) ## UPDATE TO FALSE BEFORE DEPLOYMENT

