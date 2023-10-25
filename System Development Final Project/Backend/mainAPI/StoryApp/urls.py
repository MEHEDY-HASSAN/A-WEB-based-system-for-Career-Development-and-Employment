from django.urls import re_path as url
from StoryApp import views


urlpatterns=[
    url(r'^story/$',views.storyApi),
    url(r'^story/([0-9]+)$',views.storyApi),
]