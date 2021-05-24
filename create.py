from application import db 
from application.models import User, Workout

db.drop_all()
db.create_all()