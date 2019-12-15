import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGODB_URI = os.getenv("MONGO_URI")


mongo = PyMongo(app)

@app.route('/')


@app.route('/fundamentals')
def show_fundamentals():
    return render_template('fundamentals.html', fundamentals=mongo.db.fundamental_movements.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
