from todosapp.todos.resource import TodosResource


def todos_routes(api):
    api.add_resource(TodosResource, '/api/todos', '/api/todos/<int:todo_id>')
    