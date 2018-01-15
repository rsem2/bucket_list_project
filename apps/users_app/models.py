# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def createUser(self, postData):
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = password)
        user = self.last()
        return user
    
    def registerVal(self, postData):
        results = {'errors':[], 'status': False}
        if len(postData['first_name']) < 2:
            results['status'] = True
            results['errors'].append('First name is too short')
        if len(postData['last_name']) < 2:
            results['status'] = True
            results['errors'].append('Last name is too short')
        if not re.match(r'[^@]+@[^@]+\.[^@]+', postData['email']):
            results['status'] = True
            results['errors'].append('Email is not in an acceptable format')
        if len(postData['password']) < 6:
            results['status'] = True
            results['errors'].append('Password is too short')
        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Passwords did not match')
        try:
            self.get(email = postData['email'])
            results['status'] = True
            results['errors'].append('Email is already registered')
        except:
            pass
        return results
    
    def loginVal(self, postData):
        results = {'errors':[], 'status': False, 'user': None}
        email_matches = self.filter(email = postData['email'])
        if len(email_matches) == 0:
            results['errors'].append('Please check your email and try again.')
            results['status'] = True
        else:
            results['user'] = email_matches[0]
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('That email does not match the password registered in the database.')
                results['status'] = True
        return results

    def friend_validation(self, user1, user2):
        results = {'errors':[], 'status':True}
        if user1 == user2:
            results['status'] = False
            results['errors'] = ['You cannot be friends with yourself']
        for x in UserFriends.objects.filter(friend_of = user1):
            num2 = int(user2.id)
            if (x.friend_to_id == num2):
                results['status'] = False
                results['errors'] = ['They are already friends']
        return results

    def create_friends(self, user1, user2):
        UserFriends.objects.create(friend_of = user1, friend_to = user2)
        UserFriends.objects.create(friend_of = user2, friend_to = user1)

    def delete_friend(self, user1, user2):
        UserFriends.objects.get(friend_to = user1, friend_of = user2).delete()
        UserFriends.objects.get(friend_to = user2, friend_of = user1).delete()


class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    admin = models.IntegerField(default = 1)
    profile_picture = models.ImageField(null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    friends = models.ManyToManyField("self", through = "UserFriends", related_name="friends_of", symmetrical=False)

class UserFriends(models.Model):
    friend_of = models.ForeignKey(User, related_name = "source")
    friend_to = models.ForeignKey(User, related_name = "target")
    objects = UserManager()