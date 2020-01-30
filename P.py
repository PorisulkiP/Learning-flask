from flask import Flask, render_template, request, redirect, url_for
from moduls import add_user
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

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
        return redirect(url_for('user_page', name = name))
    return render_template('index.html')

@app.route('/user/<name>')
def user_page(name):
    return render_template('users.html', username = name.title())

app.run(debug = True)