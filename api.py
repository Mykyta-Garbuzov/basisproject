from flask import Flask, request, jsonify
from flask import render_template
import os
import config
from models import Person
from flask_cors import CORS, cross_origin


app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

CORS(app.app)


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)


app.run(host='0.0.0.0', port=os.getenv('PORT'))
