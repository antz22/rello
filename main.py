import pyrebase
from flask import Flask, render_template, request, redirect, session
import os

config = {
    '': ''
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app = Flask(__name__)


@app.route('/')
def homeone():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        email = request.form['name']
        password = request.form['password']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return redirect('/index')
        except:
            unsuccessful = 'Please check your credentials'
            return render_template('login.html', umessage=unsuccessful)
    return render_template('login.html')


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if (request.method == 'POST'):
        email = request.form['name']
        password = request.form['password']
        if len(password) >= 6:
            auth.create_user_with_email_and_password(email, password)
        else:
            return render_template('create_account.html', umessage="Password must be above 6 characters.")
        return render_template('login.html')
    return render_template('create_account.html')


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if (request.method == 'POST'):
        email = request.form['name']
        auth.send_password_reset_email(email)
        return render_template('login.html')
    return render_template('forgot_password.html')


@app.route('/index', methods=['GET', 'POST'])
def home():

    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(
        'hahahackphs@gmail.com', 'testing123123')
    db = firebase.database()

    risky_incidents_f = db.child("users").child(
        "John").get().val()['risky-incidents']
    timestamp_f = db.child("users").child("John").get().val()['timestamp']
    hoursnmin_f = timestamp_f[-8:]

    return render_template('index.html', timestamp=timestamp_f, risky_incidents=risky_incidents_f, hoursnmin=hoursnmin_f)


if __name__ == '__main__':
    app.run(port=8000, debug=True)

