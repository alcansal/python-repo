from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect

# home route
@app.route('/')
def home():
    all_users = User.get_all()
    return render_template('html/index.html', all_users=all_users)

# create user form route
@app.route('/user/create')
def create_user():
    return render_template('html/create.html')

# delete user route
@app.route('/user/delete/<int:user_id>')
def delete_route(user_id):
    data = {
        "id": user_id
    }
    User.delete(data)
    return redirect('/')

# form reroute 