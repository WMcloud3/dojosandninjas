from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

@app.route("/dojos")
def dojo():
    return render_template("new_dojo.html", all_dojos = Dojo.all_dojos())

@app.route("/new_dojo", methods=["POST"])
def register_dojo():

    data = {
        "name": request.form['name'],
    }
    Dojo.save(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def one_dojo(id):
    data = {
        "id" : id
    }
    return render_template("dojo_info.html", dojo = Dojo.dojo_info(data))
