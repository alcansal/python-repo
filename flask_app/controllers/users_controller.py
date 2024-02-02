from flask_app import app
from flask_app.models.user import User
from flask import render_template

@app.route('/')
def home():
    all_users = User.get_all()
    return render_template('html/index.html', all_users=all_users)

# provide new routes