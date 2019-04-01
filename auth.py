import pickle
import random
import string
from getpass import getpass

def get_credentials():
    username = input("Enter username:")
    password = getpass("Enter password:")
    return (username, password)

def password_hash(password, salt):
    hash = 0
    for i in password+salt:
        hash += ord(i)
    return hash

def get_salt():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))


def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        salt = pwdb[username][0]
        hash = password_hash(password,salt)
        if hash == pwdb[username][1]:
            status = True
        else:
            print('Wrong password!')
    else:
        salt = get_salt()
        hash = password_hash(password,salt)
        add_user(username, salt, hash, pwdb)

    return status

def add_user(username, salt, hash, pwdb):
    pwdb[username] = [salt, hash]
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


if __name__ == "__main__":
    username, password = get_credentials()
    pwdb = read_pwdb()
    status = authenticate(username, password, pwdb)
    if status:
        print('Authentication succeeded:', pwdb)
    else:
        print('Authentication failed')
