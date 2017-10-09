""" url patterns for ms pages """
from django.conf.urls import url
from . import views

urlpatterns = [
    #Home page
    url(r'^$', views.home, name='home'),
    #All topics page
    url(r'^topics/$', views.topics, name='topics'),
    #individual topic page
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #New topic for user to create
    url(r'^new_topic/$', views.new_topic, name = 'new_topic'),
    #New entry for user to create
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = 'new_entry'),
    #Page for user to edit an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name = 'edit_entry'),
    
    ]
