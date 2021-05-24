from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask.helpers import url_for

from application import app, db
from application.models import User, Workout

class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
        app.config["LIVESERVER_PORT"] = 5050
        app.config['SECRET_KEY'] = "khanx"
        app.config["DEBUG"] = True
        app.config["TESTING"] = True
        return app
    
    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all()
        self.driver.get(f"http://localhost:5050/")

    def tearDown(self):
        self.driver.quit()
        db.drop_all()

    def test_server_is_running(self):
        response = urlopen("http://localhost:5050/")
        self.assertEqual(response.code, 200)

class TestViews(TestBase):

    def test_navigation(self):
        self.driver.find_element_by_xpath("/html/body/form[2]").click()
       
        print(url_for("create"))
        print(self.driver.current_url)
        self.assertIn(url_for("create"), self.driver.current_url)