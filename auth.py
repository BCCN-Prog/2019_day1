import pickle
from getpass import getpass
import random
import string

charset = string.ascii_letters + string.digits + string.punctuation  

def get_credentials():
    username = input("Enter username:")
    password = getpass("Enter password:")
    return (username, password)

def authenticate(username, password, pwdb):
    status = 0
    if username in pwdb:
        salt = pwdb[username]["salt"]
        if pwhash(salt+password) == pwdb[username]["password"]:
            status = 1
        else:
            pass
    else:
        add_user(username, password, pwdb)
        status = 2

    return status

def add_user(username, password, pwdb):
    salt = get_salt()
    pwdb[username] = {"password": pwhash(salt+password), "salt": salt}
    write_pwdb(pwdb)

def read_pwdb():
    try:
        with open("pwdb.pkl", "rb") as fh:
            pwdb = pickle.load(fh)
    except FileNotFoundError:
        pwdb = {}

    return pwdb

def write_pwdb(pwdb):
    with open("pwdb.pkl", "wb") as fh:
        pickle.dump(pwdb, fh)

def pwhash(pwd):
    sum = 0
    for c in pwd:
        sum += ord(c)
    return sum

def get_salt():
    return "".join(random.sample(charset,5))


if __name__ == "__main__":
    username, password = get_credentials()
    pwdb = read_pwdb()
    status = authenticate(username, password, pwdb)
    if status == 1:
        print('Authentication succeeded:', pwdb)
    elif status == 2:
        print("New user created")
    else:
        print('Authentication failed')
