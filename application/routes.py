from application import app, db


from flask import render_template, url_for, redirect, request
from application.forms import WorkoutForm, UserForm
from application.models import Workout, User


@app.route('/')
@app.route('/home')
def home():
    all_users = User.query.all()
    return render_template('index.html', all_users = all_users)



@app.route('/create', methods=['GET', 'POST'])
def create():
    form = UserForm()
    if request.method=='POST':
        if form.validate_on_submit():
            user = User(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                age = form.age.data,
                weight = form.weight.data
            )
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('create.html', subheading = 'New Member', form=form)



@app.route('/<int:userID>/workout-list' , methods=['GET', 'POST'])
def workoutList(userID):
    all_workouts = Workout.query.filter_by(user_id=userID)
    return render_template ('workoutList.html', subheadings = "List of Workouts", all_workouts=all_workouts, userID=userID)


@app.route('/<int:userID>/workout-list/add', methods=['GET','POST'])
def addWorkout(userID):
    form = WorkoutForm()
    if form.validate_on_submit():
        workout = Workout(
            workout_name = form.workout_name.data,
            workout_complete = form.workout_complete.data,
            user_id = userID
        )
        db.session.add(workout)
        db.session.commit()
        return redirect(url_for('workoutList', userID=userID))
    return render_template('addWorkout.html', subheading = 'Add Workout', form=form)



@app.route('/<int:userID>/workout-list/update/<int:workoutID>', methods=['GET','POST'])
def update(userID, workoutID):
    form = WorkoutForm()
    workout = Workout.query.filter_by(id=workoutID).first()
    if request.method == 'GET':
        form.workout_name.data = workout.workout_name
        form.workout_complete.data = workout.workout_complete
    elif request.method == 'POST':
        workout.workout_name = form.workout_name.data
        workout.workout_complete = form.workout_complete.data
        db.session.commit()
        return redirect(url_for('workoutList', userID=userID))
    return render_template('update.html', subheading='Update Page', workout=workout, userID=userID, form=form)   



@app.route("/<int:userID>/workout-list/delete/<int:workoutID>" , methods=['GET', 'POST'])
def delete(userID, workoutID):
    workout = Workout.query.filter_by(id=workoutID).first()
    db.session.delete(workout)
    db.session.commit()
    return redirect(url_for('workoutList', userID=userID))
