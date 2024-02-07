from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request

# home route
@app.route('/')
def home():
    all_users = User.get_all()
    return render_template('html/index.html', all_users=all_users)

# show one route
@app.route('/user/show/<int:user_id>')
def show_one(user_id):
    data = {
        "id": user_id
    }
    user = User.show_one(data)
    return render_template('html/show_one.html', user=user)


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
@app.route('/create/form', methods=['POST'])
def create_form():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.create(data)
    return redirect('/')