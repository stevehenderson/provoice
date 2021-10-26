users = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
]


def authenticate(username, password):
    user = {u.username: u for u in users}
    if user is not None and user.password == password: # you can delete 'is not none' because it's implied
        return user

# def identity(payload): # unique to Flask-JWT
#     user_id = {u.id: u for u in users}
#     return user_id



# set/dict comprehension
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}