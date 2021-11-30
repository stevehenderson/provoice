from user import User

users = [
    User(1, 'joe', 'badger-hint-uproar-trout!'),
    User(1, 'susan', 'badger-hint-uproar-trout!'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and (user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
