from flask_app import app
from flask_app.models.user import User
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')