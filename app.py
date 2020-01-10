import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import env

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/fundamentals')
def show_fundamentals():
    return render_template('fundamentals.html', fundamentals=mongo.db.fundamental_movements.find())


@app.route('/public-sessions')
def show_public_sessions():
    return render_template('public-sessions.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)