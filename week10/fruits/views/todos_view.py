from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from fruits.models import Todo

todos = Blueprint('todos', __name__, url_prefix='/todos')


@todos.route('/')
def index():
    if current_user.is_authenticated:
        user_todos = Todo.get_todos_by_user_id(current_user.id)
        return render_template('todos/index.html', todos=user_todos)
    else:
        return redirect(url_for('users.login'))



@todos.route('/create', methods=['POST'])
@login_required
def create():
    todo = request.form.get('todo')
    new_todo = Todo(todo=todo, created_by=current_user.id)
    new_todo.save()
    flash('Todo created successfully')
    return redirect(url_for('todos.index'))


@todos.route('/<int:todo_id>/delete', methods=['POST'])
@login_required
def delete(todo_id):
    todo = Todo.get_by_id(todo_id)
    if todo and todo.created_by == current_user.id:
        todo.delete_instance()
        flash('Todo deleted successfully')
    else:
        flash('Todo not found')
    return redirect(url_for('todos.index'))