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

    def test_login_user(self):
        self.app.post("/api/register", json=test_user)
        response = self.app.post("/api/login", json={"email": test_user['email'], "password": test_user['password']})
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token".encode(), response.data)
        self.assertIn("refresh_token".encode(), response.data)

    def test_get_todos(self):
        self.app.post("/api/register", json=test_user)
        response = self.app.post("/api/login", json={"email": test_user['email'], "password": test_user['password']})
        access_token = response.json['access_token']
        response = self.app.get("/api/todos", headers={"Authorization": f"Bearer {access_token}"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_todo(self):
        self.app.post("/api/register", json=test_user)
        response = self.app.post("/api/login", json={"email": test_user['email'], "password": test_user['password']})
        access_token = response.json['access_token']
        response = self.app.post("/api/todos", \
        headers={"Authorization": f"Bearer {access_token}"}, \
         json={"title": "test todo", "description": "test description", "due_date": "2022-10-10"})
        self.assertEqual(response.status_code, 201)



if __name__ == "__main__":
    unittest.main()
