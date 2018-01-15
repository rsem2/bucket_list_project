from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.profile),
    url(r'^/add_activity$', views.new_activity),
    url(r'^/add_activity/(?P<num>[0-9]+)$', views.add_activity),
    url(r'^/add_people/(?P<num>[0-9]+)$', views.add_people),
    url(r'^/remove_person/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)$', views.remove_person),
    url(r'^/edit_remove_person/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)$', views.edit_remove_person),
    url(r'^/process_activity_edit/(?P<num>[0-9]+)$', views.process_activity_edit),
    url(r'^/submit_post/(?P<num>[0-9]+)$', views.add_post),
    url(r'^/remove_post/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)$', views.remove_post),
    url(r'^/(?P<num>[0-9]+)$', views.friend),
    url(r'^/activity/(?P<num>[0-9]+)$', views.activity),
    url(r'^/add_idea$', views.add_idea),
    url(r'^/idea_process$',views.idea_process),
    url(r'^/idea/(?P<num>[0-9]+)$', views.idea),
    url(r'^/stats$', views.stats),
    url(r'^/ideas$', views.ideas),
    url(r'^/process_activity$', views.process_activity),
    url(r'^/edit_activity/(?P<num>[0-9]+)$', views.edit_activity),
    url(r'^/edit_idea/(?P<num>[0-9]+)$', views.edit_idea),
    url(r'^/edit_idea_process/(?P<num>[0-9]+)$', views.process_edit_idea),
    url(r'^/completed_activity_confirmation/(?P<num>[0-9]+)$', views.completed_activity_confirmation),
   
    
    # url(r'^/submit_review/(?P<num>[0-9]+)$', views.review),
    # url(r'^/submit_post/(?P<num>[0-9]+)$', views.post),
]