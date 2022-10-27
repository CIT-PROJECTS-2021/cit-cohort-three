from datetime import datetime
from todosapp.models import Todo
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse

from todosapp.schemas.app_schemas import TodoSchema

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

# Todos Resource
class TodosResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    @jwt_required()
    def post(self):
        self.parser.add_argument('title', type=str, required=True, help='Title cannot be blank')
        self.parser.add_argument('description', type=str, required=True, help='Description cannot be blank')
        self.parser.add_argument('due_date', type=str, required=True, help='Due date cannot be blank')

        data = self.parser.parse_args()

        # create date object from string => needed by sqlite db
        data['due_date'] = datetime.strptime(data['due_date'], '%Y-%m-%d')

        user_id = get_jwt_identity()

        new_todo = Todo(**data, created_by=user_id)
        new_todo.save()
        return {'message': 'Todo created successfully'}, 201

    @jwt_required()
    def get(self, todo_id=None):
        if todo_id:
            todo = Todo.get_todo_by_id(todo_id)
            if todo:
                return todo_schema.dump(todo), 200
            return {'message': 'Todo not found'}, 404

        user_id = get_jwt_identity()
        user_todos = Todo.get_user_todos(user_id)
        return todos_schema.dump(user_todos), 200

    
    @jwt_required()
    def put(self, todo_id):
        # While updating a todo, all fields are optional
        self.parser.add_argument('title', type=str)
        self.parser.add_argument('description', type=str)
        self.parser.add_argument('due_date', type=str)
        self.parser.add_argument('complete', type=bool)
        
        todo = Todo.get_todo_by_id(todo_id)

        if not todo:
            return {'message': 'Todo not found'}, 404

        # check for ownership
        if todo.created_by != get_jwt_identity():
            return {'message': 'You are not authorized to update this todo'}, 401

        data = self.parser.parse_args()

        # update todo if there is new data else keep the old data
        todo.title = data['title'] if data['title'] else todo.title
        todo.description = data['description'] if data['description'] else todo.description
        todo.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d') if data['due_date'] else todo.due_date
        todo.complete = data['complete'] if data['complete'] else todo.complete
        todo.update()

        # return updated todo
        return todo_schema.dump(todo), 200


    @jwt_required()
    def delete(self, todo_id):
        todo = Todo.get_todo_by_id(todo_id)

        if not todo:
            return {'message': 'Todo not found'}, 404

        # check for ownership
        if todo.created_by != get_jwt_identity():
            return {'message': 'You are not authorized to delete this todo'}, 401

        todo.delete()
        return {'message': 'Todo deleted successfully'}, 200

        
