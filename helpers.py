"""
Author: Jake Wachs
Generic helper functions for app.py

2/19/2020
"""

from objects.User import User

def createNewUser(content):
    """
    Creates a new User object
    """
    newUser = User()
    newUser.setUsername(content['username'])
    newUser.setEmail(content['email'])
    newUser.setPassword(content['password'])

    return newUser


def createDict(users):          # FIXME: change this to make a dict of ANY type, not just users
    """
    Creates a dictionary out of a cursor of users
    for easy conversion to JSON
    """
    userList = []
    for user in users:
        userList.append({'username' : user['username'], \
            'email' : user['email'], 'password' : user['passHash']})

    return userList
