from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection (works for Docker & local)
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(MONGO_URL)

db = client["userdb"]
collection = db["users"]

@app.route("/")
def home():
    users = collection.find()
    return render_template("index.html", users=users)

@app.route("/add", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("email")

    if name and email:
        collection.insert_one({
            "name": name,
            "email": email
        })

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

