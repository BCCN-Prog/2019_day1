import pickle
import string
import random
from getpass import getpass


def hash_password(password):
    hash_sum = 0
    for letter in password:
        hash_sum += ord(letter)
    return hash_sum


def get_credentials():
    username = input("Enter username:")
    password = getpass("Enter password:")
    return (username, password)


def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        if hash_password(password + pwdb[username][1]) == pwdb[username][0]:
            status = True
        else:
            print('Wrong password!')
    else:
        add_user(username, password, pwdb)

    return status


def add_user(username, password, pwdb):
    check = False
    while check not in ['y', 'n']:
        check = input("Do you want to add a user with these credentials? (y/n)")
        if check == 'y':
            salt = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            hashed_password = hash_password(password + salt)
            pwdb[username] = [hashed_password, salt]
            write_pwdb(pwdb)
        elif check == 'n':
            print("ByeBye!")


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
