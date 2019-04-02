import pickle
import os

from getpass import getpass

def get_credentials():
    username = input("Enter username:")
    password = getpass("Enter password:")
    return (username, password)

def pwhash(password, salt):
    hashsum = 0
    for char in password:
        hashsum += ord(char)
    return hashsum

def create_salt():
    return os.urandom(5).hex()

def authenticate(username, password, pwdb):
    status = 0
    if username in pwdb:
        password_hash, salt = pwdb[username]
        if pwhash(password, salt) == password_hash:
            status = 1
    else:
        add_user(username, password, pwdb)
        status = 2
    return status

def add_user(username, password, pwdb):
    salt = create_salt()
    pwdb[username] = [pwhash(password, salt), salt]
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
    if status == 1:
        print('Authentication succeeded:', pwdb)
    elif status == 2:
        print("Registered new user")
    else:
        print('Authentication failed')
