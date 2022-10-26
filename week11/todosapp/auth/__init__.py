from todosapp.auth.resource import Login

def auth_routes(api):
    api.add_resource(Login, '/api/login')