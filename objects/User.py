"""
Author: Jake Wachs
User object

12/7/2019
"""

import json

class User:
    def __init__(self):
        """
        Instantiate User object, default constructor
        """
        print('Instantiating new user object')

    def setUsername(self, n):
        """
        Setter for name
        """
        self.username = n


    def getUsername(self):
        """
        Getter for name
        """
        return self.username


    def setPassword(self, p):
        """
        Setter for password
        """
        self.password = p


    def getPassword(self):
        """
        Getter for password
        """
        return self.password


    def encryptPassword(self):
        """
        Encrypts the password returns string
        """
        print('FIXME')          # FIXME: add encryption to app!

    def setPassHash(self, hash):
        """
        Setter for password hash
        """
        self.passHash = hash


    def getPassHash(self):
        """
        Getter for password hash
        """
        return self.passHash;


    def setEmail(self, email):
        """
        Setter for user email
        """
        self.email = email


    def getEmail(self):
        """
        Getter for user email
        """
        return self.email

    def getDict(self):
        """
        Converts class to dictionary and jsonify's
        """
        user_dict = {
            "username": self.username,
            "email": self.email,
            "passHash": self.password
        }

        return user_dict


    def insertDB(self, collection):
        """
        Inserts object's info to database
        """
        dict = self.getDict()
        # print(dict)
        collection.insert_one(dict)
