from flask import  request, session, make_response, redirect, render_template,url_for, flash
import unittest
from flask_login import login_required, current_user

from app import create_app
from app.forms import TodoForm
from app.firestore_service import get_users, getj_todos, put_todo

app = create_app()

todos = ['comprar juego', 'solicitud de compra','entrgar video']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error = error)

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
@app.route('/')
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()

    context  = {
        'user_ip' : user_ip,
        'todos' : getj_todos(user_id=username),
        'username': username,
        'todo_form': todo_form
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data, game=todo_form.game.data, price=todo_form.price.data)

        flash(' tu juego se ha agregado')

        return redirect(url_for('hello'))
        
    return render_template('hello.html', **context)