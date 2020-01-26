import os
import datetime
from os import path
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
from forms import LoginForm, RegisterForm, CreateWorkoutForm, EditWorkoutForm, DeleteForm

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
get_workouts = mongo.db.workouts


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/fundamentals')
def show_fundamentals():
    return render_template('fundamentals.html', fundamentals=mongo.db.fundamental_movements.find())


@app.route('/public-workouts')
def show_public_workouts():
    return render_template('public-workouts.html', workouts=mongo.db.workouts.find())


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        found_username = users.find_one({'username': request.form['username']})

        if found_username:
            if bcrypt.check_password_hash(found_username['password'], request.form.get('password').encode('utf-8')):
                session['username'] = request.form.get('username')
                session['logged-in'] = True
                return redirect(url_for('my_workouts'))
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


@app.route('/create-workout', methods=['GET', 'POST'])
def create_workout():
    create_workout_form = CreateWorkoutForm()

    if request.method == 'POST':
        get_workouts.insert_one({
            'username': session['username'],
            'date': datetime.datetime.utcnow().strftime('%H:%M:%S - %d/%m/%Y'),
            'location_name': create_workout_form.location_name.data,
            'focus_name': create_workout_form.focus_name.data,
            'part_a': create_workout_form.part_a.data,
            'part_b': create_workout_form.part_b.data,
            'part_c': create_workout_form.part_c.data,
            'accessory': create_workout_form.accessory.data,
            'additional_info': create_workout_form.additional_info.data,
            'coach_notes': create_workout_form.coach_notes.data,
            'public_workout': create_workout_form.public_workout.data,
        })
        flash(f'Workout added.', 'primary')
        return redirect(url_for('index', title='Workout Added'))

    focus_type = mongo.db.focus_type.distinct('focus_name')
    create_workout_form.focus_name.choices = [('', 'Please select')] + [(focus, focus) for focus in focus_type]
    location_type = mongo.db.location.distinct('location_name')
    create_workout_form.location_name.choices = [('', 'Please select')] + [(locale, locale) for locale in location_type]

    return render_template('create-workout.html', form=create_workout_form)


@app.route('/my-workouts')
def my_workouts():
    return render_template('my-workouts.html', workouts=mongo.db.workouts.find())


@app.route('/workout-view/<workout_id>')
def workout_view(workout_id):
    my_workout = get_workouts.find_one({'_id': ObjectId(workout_id)})
    return render_template('workout-view.html', workout=my_workout)


@app.route('/edit-workout/<workout_id>', methods=['GET', 'POST'])
def edit_workout(workout_id):
    my_workout = get_workouts.find_one({'_id': ObjectId(workout_id)})
    if request.method == 'GET':
        edit_workout_form = EditWorkoutForm(data=my_workout)
        return render_template('edit-workout.html', workout=my_workout, form=edit_workout_form)

    edit_workout_form = EditWorkoutForm(request.form)
    if request.method == 'POST':
        my_workout.update_one({
            'id': ObjectId(workout_id),
        }, {
            '$set': {
                'location_name': edit_workout_form.location_name.data,
                'focus_name': edit_workout_form.focus_name.data,
                'part_a': edit_workout_form.part_a.data,
                'part_b': edit_workout_form.part_b.data,
                'part_c': edit_workout_form.part_c.data,
                'accessory': edit_workout_form.accessory.data,
                'additional_info': edit_workout_form.additional_info.data,
                'coach_notes': edit_workout_form.coach_notes.data,
                'public_workout': edit_workout_form.public_workout.data,
            }
        })
        flash(f'Workout Updated', 'primary')
        return redirect(url_for('index', title='Workout Updated'))
    return render_template('edit-workout.html', workout=my_workout)


@app.route('/delete-workout/<workout_id>', methods=['GET', 'POST'])
def delete_workout(workout_id):
    my_workout = get_workouts.find_one({'_id': ObjectId(workout_id)})

    delete_workout_form = DeleteForm()
    if request.method == 'POST':
        if session['username'] == request.form.get('username'):
            get_workouts.remove({'_id': ObjectId(workout_id)})
            flash(f'Workout removed.', 'primary')
            return redirect(url_for('index', title='Workout Removed'))

    return render_template('delete-workout.html', workout=my_workout, form=delete_workout_form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=os.environ.get('PORT', '5000'),
            debug=True)
