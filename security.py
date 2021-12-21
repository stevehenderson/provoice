import json
import sqlite3 
from user import User

conn = sqlite3.connect('database/provoice.db')
print(conn)
cursor = conn.execute("SELECT id, username, password from users")

users = []
for row in cursor:
    print(row)
    a_user = User(row[0], row[1], row[2])
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
