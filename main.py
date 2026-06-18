from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]
collection = db["students"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student = {
            "name": request.form["name"],
            "email": request.form["email"],
            "course": request.form["course"]
        }
        collection.insert_one(student)
        return redirect(url_for("index"))

    students = collection.find()
    return render_template("index.html", students=students)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    student = collection.find_one({"_id": ObjectId(id)})

    if request.method == "POST":
        collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "name": request.form["name"],
                "email": request.form["email"],
                "course": request.form["course"]
            }}
        )
        return redirect(url_for("index"))

    return render_template("edit.html", student=student)

@app.route("/delete/<id>")
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)