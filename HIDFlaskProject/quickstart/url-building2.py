from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return 'Hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def profile(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))