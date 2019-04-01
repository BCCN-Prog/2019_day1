import pickle
from getpass import getpass
import random as rnd
import string

def get_credentials():
    username = input("Enter username:")
    password = getpass("Enter password:")
    return (username, password)

def get_hash(password, salt):
    hash_sum = 0
    for character in password:
        hash_sum += ord(character)
    for character in salt:
        hash_sum += ord(character)
    return hash_sum

def get_salt():
    salt = []
    for i in range (10):
        character = rnd.choice(string.ascii_lowercase)
        salt.append(character)
    return ''.join(salt)

def authenticate(username, password, pwdb):
    status = 0
    if username in pwdb:
        salt = pwdb[username][0]
        pass_hash = pwdb[username][1]
        if get_hash(password, salt) == pass_hash:
            status = 1
    else:
        add_user(username, password, pwdb)
        status = 2

    return status

def add_user(username, password, pwdb):
    new_salt = get_salt()
    pwdb[username] = (new_salt, get_hash(new_salt, password))
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
    if status == 0:
        print('Username taken, authentication failed.')
    if status == 1:
        print('Authentication succeeded:', pwdb)
    if status == 2:
        print('Username not in database, added.')

