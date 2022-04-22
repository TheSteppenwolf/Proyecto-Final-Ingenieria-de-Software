from app import app
from flask import render_template, url_for, flash, get_flashed_messages, redirect, request
from datetime import datetime

@app.route("/")
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/soluciones", methods=["GET"])
def soluciones():
    return render_template("soluciones.html")

@app.route("/documentacion", methods=["GET"])
def documentacion():
    return render_template("documentacion.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")