from user import User

users = [User(1, 'bob', 'asdf' )]


username_mapping = { u.username: u for u in users} #looping through users list, we make the username(bob) the key. 
#The values of the key are the objects "bob" class properties


userid_mapping = { u.id: u for u in users} # the key:value pair in here is the id is the key, bobs propties are the value


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

