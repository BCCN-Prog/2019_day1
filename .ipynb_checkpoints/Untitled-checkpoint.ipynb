{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter username:ghy\n",
      "Enter password:········\n",
      "Authentication failed\n"
     ]
    }
   ],
   "source": [
    "# %load auth.py\n",
    "import pickle\n",
    "import getpass\n",
    "import string\n",
    "import random\n",
    "\n",
    "def get_credentials():\n",
    "    username = input(\"Enter username:\")\n",
    "    password = getpass.getpass(\"Enter password:\")\n",
    "    return (username, password)\n",
    "\n",
    "def salt_generator():\n",
    "    # creating random string of size 10\n",
    "    chars = string.ascii_uppercase + string.ascii_lowercase\n",
    "    return ''.join(random.choice(chars) for _ in range(10))\n",
    "\n",
    "def count_password(pswd_salt):\n",
    "    # for creating hash function\n",
    "    # counting the ascii values of each character of password\n",
    "    count =0\n",
    "    for c in pswd_salt:\n",
    "        count = count + ord(c)\n",
    "    return count\n",
    "                   \n",
    "def authenticate(username, password, pwdb):\n",
    "    status = False\n",
    "    if username in pwdb:\n",
    "        if password == pwdb[username]:\n",
    "            status = True\n",
    "        else:\n",
    "            print('Wrong password!')\n",
    "    else:\n",
    "        add_user(username, password, pwdb)\n",
    "\n",
    "    return status\n",
    "\n",
    "def add_user(username, password, pwdb):\n",
    "    pwdb[username] = password\n",
    "    write_pwdb(pwdb)\n",
    "\n",
    "def read_pwdb():\n",
    "    try:\n",
    "        with open(\"pwdb.pkl\", \"rb\") as fh:\n",
    "            pwdb = pickle.load(fh)\n",
    "    except FileNotFoundError:\n",
    "        pwdb = {}\n",
    "\n",
    "    return pwdb\n",
    "\n",
    "def write_pwdb(pwdb):\n",
    "    with open(\"pwdb.pkl\", \"wb\") as fh:\n",
    "        pickle.dump(pwdb, fh)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    username, password = get_credentials()\n",
    "    pwdb = read_pwdb()\n",
    "    # Need to modify..One constant salt for a username\n",
    "    salt_val = salt_generator()\n",
    "    \n",
    "    pswd_salt = password+salt_val\n",
    "            \n",
    "    hash_val = count_password(pswd_salt)\n",
    "    \n",
    "    status = authenticate(username, hash_val, pwdb)\n",
    "    if status:\n",
    "        print('Authentication succeeded:', pwdb)\n",
    "    else:\n",
    "        print('Authentication failed')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
