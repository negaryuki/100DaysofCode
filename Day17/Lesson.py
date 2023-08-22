# A class is like a object creator or a "blueprint" for creating objects in python.


# How to create a class --->   class ClasName:


class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

# if we want to not repeat an assigned value to the class, we don't mention it after the __init__


# a Method, unlike a function, always needs a "self" parameter first, below the "user" is the one we decide to follow.

# this means that the user we are following "user" will have one more "follower". and we "self" will have one more "following".

    def follow (self,user):
        user.followers += 1
        self.following += 1


# Using Class to create an object: to do so, we have to asign the class to a variable


user1 = User('001', 'Negar')
user2 = User('003', 'Angela')

print(user2.name)

user1.follow(user2)

print(user2.name , user2.followers , user2.following)

print(user1.name , user1.followers, user1.following)
