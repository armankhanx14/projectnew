from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.core import DecimalField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired

from application.models import Workout

class WorkoutForm(FlaskForm):

    workout_name = SelectField('Workout Name', choices= [("Squats", "Squats"), ("Deadlifts","Deadlifts"), ("Military Press","Military Press"),("Bench Press", "Bench Press"), ("Calisthenics","Calisthenics") ],
        validators =[ 
            DataRequired()
        ])
    
    workout_complete = BooleanField('Workout Complete',
        validators = [
             DataRequired()
        ])

    submit = SubmitField('Submit')

#Flask Form Classes
class UserForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            DataRequired()
        ])
    last_name = StringField('Last Name',
        validators = [
            DataRequired()
        ])
    age = IntegerField('Age',
        validators = [ 
            DataRequired()
        ])
    weight = DecimalField('Weight (KG)',
        validators = [
             DataRequired()
        ])

    submit = SubmitField('Submit')


    
#flask Form Classes End