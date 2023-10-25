from django.urls import re_path as url
from FollowApp import views

urlpatterns=[
    url(r'^follow/([0-9]+)$',views.followApi),
    url(r'^follow/([0-9]+)/([0-9]+)$',views.followApi),

    url(r'^active/([0-9]+)$',views.activeApi),
]