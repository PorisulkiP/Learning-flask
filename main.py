from flask import (Flask, render_template, request, 
                   redirect, url_for, session, flash)
from moduls import add_user, check_user, add_task, Task, get_user_task, delete_task, change_task
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.secret_key = 'LedyGagA'


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['pass']
        password_check = request.form['pass_check']
        if password != password_check:
            return render_template('index.html', error = 'passwords_not_match')
        try:
            add_user(name, email, password)
        except IntegrityError:
            return render_template('index.html', error = 'already_exists')
        session['username'] = name
        return redirect(url_for('user_page', name = name))
    return render_template('index.html')

@app.route('/user/<name>')
def user_page(name):
    if request.method == 'POST':
        title = request.form['title']
        details = request.form['details']
        deadline_date = request.form['deadline_date']
        add_task(session['username'], title, details, deadline_date)
    user_task = get_user_task(name)
    return render_template('users.html', username = name.title(), tasks=user_task)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        user = check_user(email, password)
        if user:
            session['username'] = user.name
            return redirect(url_for('user_page', name = user.name)) 
        else:
            return render_template('login.html', error = True)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/remove/<task_id>')
def delete_tasks(task_id):
    delete_task(session['username'],task_id)
    flash(f'{task_id} was deleted')
    return redirect(url_for('user_page', name = session['username']))

@app.route('/remove/task_<task_id>')
def change_tasks(task_id):
    change_task(session['username'],task_id)
    flash(f'{task_id} was changed')
    return redirect(url_for('user_page', name = session['username']))

app.run(debug = True)