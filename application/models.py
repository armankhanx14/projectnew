from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30),nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    age = db.Column(db.Integer,nullable= False)
    weight = db.Column(db.Float(10,2), nullable = False)

    workout = db.relationship('Workout', backref='user')
    
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    workout_name = db.Column(db.String(30), nullable=False)
    workout_complete = db.Column(db.Boolean, default = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


#new