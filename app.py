import os
from os import path
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
from forms import LoginForm, RegisterForm
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Secret Key value generated via secrets python module.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
users = mongo.db.users

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/fundamentals')
def show_fundamentals():
    return render_template('fundamentals.html', fundamentals=mongo.db.fundamental_movements.find())


@app.route('/public-sessions')
def show_public_sessions():
    return render_template('public-sessions.html', sessions=mongo.db.sessions.find())


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        found_username = users.find_one({'username': request.form['username']})

        if found_username:
            if bcrypt.check_password_hash(found_username['password'], request.form.get('password').encode('utf-8')):
                session['username'] = request.form.get('username')
                session['logged-in'] = True
                return redirect(url_for('my_sessions'))
            else:
                flash(f'Username or Password incorrect. Please try again.', 'danger')
                return redirect(url_for('login'))

    return render_template('login.html', title='Login', form=login_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        found_username = users.find_one({'username': request.form['username']})

        if not found_username:

            hashed_pw = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            users.insert_one({'username': register_form.username.data,
                              'password': hashed_pw})
            session['username'] = request.form.get('username')
            return redirect(url_for('index'))
        else:
            flash(f'Duplicate value detected for username. Please try another username.', 'danger')
            return redirect(url_for('register'))

    return render_template('register.html', title='Register', form=register_form)


@app.route('/logout')
def logout():
    session.clear()
    flash(f'Thank you for using Oly-Track. See you soon.', 'primary')
    return redirect(url_for('index'))


@app.route('/create-session')
def create_session():
    return render_template('create-session.html')


@app.route('/my-sessions')
def my_sessions():
    return render_template('my-sessions.html')


@app.route('/session-view')
def session_view():
    return render_template('session-view.html')


@app.route('/edit-session')
def edit_session():
    return render_template('edit-session.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)