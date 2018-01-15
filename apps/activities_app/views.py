# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Idea, Activity, Post
from ..users_app.models import User
from time import strftime
import random

# Create your views here.
def profile(request):
    user = User.objects.get(id=request.session['userid'])
    ideas = Idea.objects.all()
    print ideas
    try:
        user.activities.all()
    except:
        print 'it doesnt exist'
    else:
        print 'it does exist'
        # NOTE: exclude ideas already in your list
        # for activity in user.activities.all():
        #     ideas = ideas.exclude(id = activity.idea.id)
    idea = []
    if(len(ideas)!=0):
        if(len(ideas)<3):
            x = len(ideas)
        else:
            x=3
        numbers = []
        for i in range(0,x):
            number = random.randrange(0, len(ideas))
            while number in numbers:
                number = random.randrange(0, len(ideas))
            numbers.append(number)
            idea.append(ideas[number])
            ideas.exclude(id = ideas[number].id)
    context = {
        'user': user,
        'completed': user.activities.filter(completed=True),
        'uncompleted': user.activities.filter(completed = False),
        'idea': idea
    }
    return render(request,'profile.html', context)

def friend(request,num):
    user = User.objects.get(id=request.session['userid'])
    person = User.objects.get(id=num)
    print 
    if len(user.friends.filter(id = person.id)) == 1:
        friends = True
    else:
        friends = False
    print friends
    context = {
        'person': User.objects.get(id=num),
        'friends': friends,
        'completed': person.activities.filter(completed=True),
        'uncompleted': person.activities.filter(completed = False),
    }
    return render(request,'friend.html', context)

def add_idea(request):
    return render(request, 'new_idea.html')

def idea_process(request):
    user = User.objects.get(id = request.session['userid'])
    idea = Idea.objects.createIdea(request.POST, user)
    string = '/dashboard/idea/'+str(idea.id)
    return redirect(string)

def idea(request, num):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'idea': Idea.objects.get(id=num),
        'user': user,
        'friends': user.friends.all(),
    }
    return render(request, 'idea.html', context)

def add_activity(request, num):
    idea = Idea.objects.get(id=num)
    user = User.objects.get(id=request.session['userid'])
    activity = Activity.objects.createActivity(request.POST, idea, user)
    # return redirect('/dashboard/idea/'+num)
    string = '/dashboard/activity/'+str(activity.id)
    return redirect(string)

def new_activity(request):
    context = {
        'friends': User.objects.get(id=request.session['userid']).friends.all(),
    }
    return render(request, 'new_activity.html', context)

def process_activity(request):
    user = User.objects.get(id = request.session['userid'])
    print user
    print user.first_name
    idea = Idea.objects.createIdea(request.POST, user)
    print idea
    print idea.title
    activity = Activity.objects.createActivity(request.POST, idea, user)
    string = '/dashboard/activity/'+str(activity.id)
    return redirect(string)

def activity(request,num):
    friends = User.objects.get(id=request.session['userid']).friends.all()
    people = Activity.objects.get(id=num).people.all()
    for person in people:
        friends = friends.exclude(id = person.id)  
    context = {
        'activity': Activity.objects.get(id=num),
        'user': User.objects.get(id=request.session['userid']),
        'people': people,
        'friends': friends,
        'posts': Activity.objects.get(id=num).posts.all()
    }
    return render(request, 'activity.html', context)

def edit_activity(request,num):
    friends = User.objects.get(id=request.session['userid']).friends.all()
    people = Activity.objects.get(id=num).people.all()
    for person in people:
        friends = friends.exclude(id = person.id)  
    context = {
        'activity': Activity.objects.get(id=num),
        'user': User.objects.get(id=request.session['userid']),
        'people': people,
        'friends': friends,
        'posts': Activity.objects.get(id=num).posts.all()
    }
    return render(request, 'edit_activity.html', context)


def add_people(request,num):
    activity = Activity.objects.get(id=num)
    Activity.objects.addPeople(request.POST,activity)
    return redirect('/dashboard/activity/'+num)

def remove_person(request, num1, num2):
    activity = Activity.objects.get(id=num1)
    person = User.objects.get(id=num2)
    Activity.objects.removePerson(activity, person)
    return redirect('/dashboard/activity/'+num1)

def edit_remove_person(request, num1, num2):
    activity = Activity.objects.get(id=num1)
    person = User.objects.get(id=num2)
    Activity.objects.removePerson(activity, person)
    return redirect('/dashboard/edit_activity/'+num1)

def add_post(request, num):
    activity = Activity.objects.get(id=num)
    user = User.objects.get(id=request.session['userid'])
    Post.objects.createPost(request.POST,activity, user)
    return redirect('/dashboard/activity/'+num)

def remove_post(request, num1, num2):
    post = Post.objects.get(id=num2)
    Post.objects.removePost(post)
    return redirect('/dashboard/activity/'+num1)

def ideas(request):
    user = User.objects.get(id=request.session['userid'])
    ideas = Idea.objects.all()
    for activity in user.activities.all():
        # ideas = ideas.exclude(id = activity.idea.id)
        ideas = ideas.all()
    context = {
        'ideas': ideas,
    }
    return render(request, 'ideas.html', context)

def stats(request):
    return render(request, 'stats.html')

def process_activity_edit(request, num):
    activity = Activity.objects.get(id=num)
    Activity.objects.editActivity(request.POST, activity)
    return redirect('/dashboard/activity/'+num) 

def edit_idea(request, num):
    context = {
        'idea': Idea.objects.get(id=num),
    }
    return render(request, 'edit_idea.html', context)

def process_edit_idea(request,num):
    idea = Idea.objects.get(id=num)
    Idea.objects.editIdea(request.POST, idea)
    return redirect('/dashboard/idea/'+num)
    
def completed_activity_confirmation(request, num):
    friends = User.objects.get(id=request.session['userid']).friends.all()
    people = Activity.objects.get(id=num).people.all()
    for person in people:
        friends = friends.exclude(id = person.id)  
    context = {
        'activity': Activity.objects.get(id=num),
        'user': User.objects.get(id=request.session['userid']),
        'people': people,
        'friends': friends,
    }

    return render(request, 'complete_activity_confirmation.html', context)
