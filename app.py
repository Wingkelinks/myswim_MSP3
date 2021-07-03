import os
from flask import (
    Flask, flash, render_template, 
    redirect, request,  session, url_for)
from flask_pymongo import PyMongo
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True) ## UPDATE TO FALSE BEFORE DEPLOYMENT

