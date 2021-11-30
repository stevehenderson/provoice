import json
from user import User

#Create a secrets file -- don't check into git -- see instructions
f = open('secrets/users.json')

user_data = json.load(f)
users = []
for u in user_data:
    a_user = User(u['id'], u['username'], u['password'])
    users.append(a_user)

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and (user.password==password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
