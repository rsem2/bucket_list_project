# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..users_app.models import User
# Create your models here.
class UserManager(models.Manager):
    def createIdea(self, postData, user):
        if len(str(postData['title']))>0:         
            self.create(title = postData['title'], description = postData['description'], toughness = postData['toughness'], time = postData['time'],cost = postData['cost'], idea_creator=user)
            idea = self.last()
        else:
            idea = self.get(id = postData['idea_drop'])
        return idea
    
    def createActivity(self, postData, idea, user):  
        self.create(title = idea.title, description = idea.description, toughness = idea.toughness, time = idea.time, cost = idea.cost, completed=False, privacy=postData['privacy'], date=postData['date'], activity_creator=user)  
        activity = self.last()  
        print activity
        print postData.getlist('people[]')
        for person in postData.getlist('people[]'):
            activity.people.add(User.objects.get(id=person))
            activity.save()
        return self.last()

    def addPeople(self, postData, activity):
        for person in postData.getlist('people[]'):
            activity.people.add(User.objects.get(id=person))
            activity.save()
        return activity

    def removePerson(self, activity, person):
        activity.people.remove(person)
        return activity

    def editActivity(self, postData, activity):
        
        return activity

    def createPost(self, postData, activity, user):
        self.create(content = postData['content'], activity = activity, user = user)
        post = self.last()
        return post

    def removePost(self, post):
        post.delete()
        return


class Idea(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    toughness = models.IntegerField(max_length=1)
    time = models.IntegerField(max_length=1)
    cost = models.IntegerField(max_length=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    idea_creator = models.ForeignKey(User, related_name="ideas")
    objects = UserManager()

class Activity(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    toughness = models.IntegerField(max_length=1)
    time = models.IntegerField(max_length=1)
    cost = models.IntegerField(max_length=1)
    completed = models.BooleanField()
    privacy = models.IntegerField(max_length=1)
    date = models.DateField()
    # NOTE: add validation so that is completed date can't be in the future but if uncompleted date can't be in the past
    people = models.ManyToManyField(User, related_name="activities")
    activity_creator = models.ForeignKey(User, related_name="activities_created")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Post(models.Model):
    content = models.TextField(max_length = 1000)
    activity = models.ForeignKey(Activity, related_name="posts")
    user = models.ForeignKey(User, related_name="posts")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

# class Book(models.Model):
#     title = models.CharField(max_length = 100)
#     author = models.ForeignKey(Author, related_name="books")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     objects = UserManager()

