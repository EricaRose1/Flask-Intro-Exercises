from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    '''returns welcome'''
    return "Welcome"

@app.route('/welcome/home')
def welcome():
    '''welcome home'''
    return "Welcome home"

@app.route('/welcome/back')
def welcome():
    '''welcome back'''
    return "Welcome back"