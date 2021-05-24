from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import User, Workout


class TestBase(TestCase):
    def create_app(self):
        app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///"
        app.config['SECRET_KEY'] = "khanx"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config["DEBUG"]= True
        return app

        
    def setUp(self):
        db.create_all()

        test_workoutlist1 = User(
            first_name="arman",last_name="khan", age="24",weight="3.3")

        #test_workoutoutlist2 = Workout(workout_name="Squats",workout_complete="True")

        db.session.add(test_workoutlist1)
        #db.session.add(test_workoutoutlist2)
        db.session.commit()



    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_page_get(self):
        response = self.client.get(url_for("home"))
        print(response.data)
        self.assertIn(b"arman", response.data)        
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.get(url_for("create"))
    #print(response.data)
    #self.assertIn(b"arman", response.data)        
        self.assertEqual(response.status_code, 200)

    def test_workoutList(self):
        response = self.client.get(url_for('workoutList', userID=1))
        self.assertEqual(response.status_code, 200)

    def test_addMovie(self):
        response = self.client.get(url_for('addWorkout', userID=1))
        self.assertEqual(response.status_code, 200)
'''
    def test_update(self):
        response = self.client.get(url_for('update', userID=1, workoutID=1))
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.get(url_for('delete', userID=1, workoutID=1))
        self.assertEqual(response.status_code, 302)
        '''

class TestCreate(TestBase):
    def test_createuser(self):
        response = self.client.post(url_for("create"),
        data = dict(first_name="arman",last_name="khan",age="24",weight=3.3,
        ),
        follow_redirects=True
        ) 
        self.assertIn(b"arman",response.data),
        self.assertIn(b"khan",response.data)

class TestRead(TestBase):
    def test_read_user(self):
        response=self.client.get(url_for("home"))
        self.assertIn(b"arman", response.data)
        self.assertIn(b"khan",response.data)


'''
class TestDelete(TestBase):
    def test_delete_workout(self):
response = self.client.get(url_for("delete", userID=1, workoutID=1))
self.assertNotIn(b"Deadlifts", response.data) 
self.assertNotIn(b"True", response.data) 
'''















'''
    def test_create_get(self):

        response = self.client.get(url_for("create"))
        self.assertIn(b"Squats", response.data)
        self.assertEqual(response.status_code, 200)         
'''
