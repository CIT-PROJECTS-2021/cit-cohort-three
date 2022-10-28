import unittest
from app import app, db


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.config['SECRET_KEY'] = "testkey"
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todos_test.db"
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self) -> None:
        with app.app_context():
            db.session.remove()
            db.drop_all()

test_user = {
    "name": "test",
    "email": "test@email.com",
    "password": "testpassword"
}
   
class TodosAPITest(BaseTestCase):
    def test_register_user(self):
        response = self.app.post("/api/register", json=test_user)
        self.assertEqual(response.status_code, 201)
        self.assertIn(test_user['email'].encode(), response.data)



if __name__ == "__main__":
    unittest.main()
