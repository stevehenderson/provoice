import json
from user import User


f = open('secrets/users.json')

user_data = json.load(f)
users = []
print("HI")
for u in user_data:
    a_user = User(u['id'], u['username'], u['password'])
    print("Added user {}".format(a_user))

#users = [
#    User(1, 'user1', 'abcxyz'),
#    User(2, 'user2', 'abcxyz'),
#]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and (user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)