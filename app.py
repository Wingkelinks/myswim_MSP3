import os
from flask import (
   Flask, flash, render_template,
   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# --------------- APP CONFIGURATION --------------- #

# DB Name
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")

# Connection String
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# Secret key for Flask functions
app.secret_key = os.environ.get("SECRET_KEY")

# Create instance of PyMongo and add Flask App Object
mongo = PyMongo(app)

# --------------- FUNCTIONS --------------- #


def get_user():
    # Gets user in session
    session_user = mongo.db.users.find_one({"username": session["user"]})
    return session_user


def get_id():
    # Gets ObjectId of user in session
    user_id = str(get_user()['_id'])
    return user_id

# --------------- ROUTING --------------- #


# HOME PAGE
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# GET SETS
@app.route("/get_sets")
def get_sets():
    # Wrap 'find' method inside python list
    sets = list(mongo.db.sets.find())
    return render_template("sets.html", sets=sets)


# SEARCH SETS
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    sets = list(mongo.db.sets.find({"$text": {"$search": query}}))
    return render_template("sets.html", sets=sets, 
                           search_results="{}".format(query))


# REGISTRATION
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists within DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists - please try again.")
            return redirect(url_for("register"))
        # If no existing user is found create register dictionary
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Success! Welcome to MySwim.")
    return render_template("register.html")


# LOG IN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome to MySwim, {}!".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# PROFILE
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    sets = list(mongo.db.sets.find(
        {"created_by": session["user"]}).sort("_id", 1))
    categories = list(mongo.db.categories.find())

    if session["user"]:
        return render_template(
           "profile.html", username=username, sets=sets,
           categories=categories)

    return redirect(url_for("login"))


# LOG OUT
@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("'Till Next Time... Happy Swimming!")
    # session.pop specifically removes user cookie
    session.pop("user")
    return redirect(url_for("login"))


# USER ADD NEW SWIM SET
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
            "created_by": session["user"],
            "user_favs": 0
        }
        mongo.db.sets.insert_one(set)
        flash("Sucess! Your set has been added.")
        return redirect(url_for("get_sets"))
    # Find categories in DB and sort a-z
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_set.html", categories=categories)


# USER EDIT SWIM SET
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


# USER DELETE SWIM SET
@app.route("/delete_set/<set_id>")
def delete_set(set_id):
    # Find set
    set = mongo.db.sets.find_one({"_id": ObjectId(set_id)})

    # Remove set from DB
    mongo.db.sets.remove({"_id": ObjectId(set_id)})

    # Also remove any favourites connected to set from DB
    mongo.db.favourites.delete_many({"set_id": set_id})

    flash("Set Deleted")
    return redirect(url_for('profile', username=session['user']))


# USER ADD FAVOURITE SETS
@app.route("/add_favourite/<set_id>/<user>", methods=["GET", "POST"])
def add_favourite(set_id, user):
    # Add favourite set to users favourites
    user_id = get_id()

    if request.method == "POST":
        set = mongo.db.sets.find_one({"_id": ObjectId(set_id)})
        set_name = set['set_name']

        favourite = {
                "set_id": set_id,
                "set_name": set_name,
                "user": user_id
            }
        # Add favourites to DB
        mongo.db.favourites.insert_one(favourite)
        flash("Set Added to Favourites!")
    return redirect(url_for(
        "profile_favs", set_id=set_id, username=session['user']))


# ADD FAVS TO PROFILE
@app.route("/profile_favs/<username>")
def profile_favs(username):
    # Check DB for user favourites
    user_id = get_id()

    # Gets users favourites from DB
    favourites = list(mongo.db.favourites.find({"user": user_id}))
    # Add favourites to profile_favs
    return render_template("profile_favs.html",
                           favourites=favourites,
                           username=username, set=set)


# PRINT SET PAGE
@app.route("/print_set/<set_id>")
def print_set(set_id):
    # Extract single set and render template to print
    set = mongo.db.sets.find_one({"_id": ObjectId(set_id)})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    sets = list(mongo.db.sets.find(
        {"created_by": session["user"]}).sort("_id", 1))
    categories = list(mongo.db.categories.find())

    return render_template(
        "print_set.html", set=set, sets=sets,
        username=username, categories=categories)


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
        # Add new CAT to DB
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_content.html")


# EDIT AND DELETE CATEGORIES FOR ADMIN
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

    # Confirm admin is logged in
    if "user" not in session:
        flash("Please Log In!")
        return redirect(url_for("login"))

    # If user is not admin
    elif session["user"].lower() != "admin":
        flash("Sorry, you are not permitted to do that!")
        return redirect(url_for("get_categories"))

    else:
        if request.method != "POST":
            return render_template("edit_category.html", category=category)

        edit = {"$set": {
            "category_name": request.form.get("category_name"),
        }}

        # Update category in DB
        mongo.db.categories.update_many(category, edit)
        flash("Category Updated")
        return redirect(url_for("get_categories"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

    # If user is not admin
    if session["user"] != "admin":
        flash("Sorry, you are not permitted to do that!")
        return redirect(url_for("get_categories"))

    else:
        # Delete category from DB
        mongo.db.categories.remove(category)
        flash("Category Deleted")
        return redirect(url_for('get_categories'))


# NOT WORKING
# VIEW SETS IN ADMIN MANAGE CONTENT
@app.route("/admin_sets")
def admin_sets():
    sets = list(mongo.db.sets.find().sort("set_name", 1))
    return render_template("manage_content.html", sets=sets)


# ERROR HANDLERS
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error), 500

# UPDATE TO FALSE BEFORE DEPLOYMENT
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)