import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()

MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGODB_URI = os.getenv("MONGO_URI")

app = Flask(__name__)


@app.route('/')


@app.route('/base')
def test():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
            port = os.environ.get('PORT'),
            debug=True)
