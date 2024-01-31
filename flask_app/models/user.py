from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = 'users_crud_schema'
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # classmethods down here