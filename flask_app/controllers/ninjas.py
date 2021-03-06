from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def ninja():
    return render_template("new_ninja.html", all_dojos = Dojo.all_dojos())

@app.route("/new_ninja", methods=["POST"])
def register_ninja():

    data = {
        "dojo_id": request.form['dojo_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
    }
    Ninja.save(data)
    dojo_id = request.form['dojo_id']

    return redirect(f"/dojos/{dojo_id}")