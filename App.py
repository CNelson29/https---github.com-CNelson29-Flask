from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/index')
def index():
    return 'ya te has registrado, funciono!!!!'

@app.route('/')
def login():
    return render_template('login.html')