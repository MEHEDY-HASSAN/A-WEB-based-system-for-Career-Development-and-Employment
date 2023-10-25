from django.urls import re_path as url
from MessageApp import views

urlpatterns=[
    url(r'^message/([0-9]+)/([-]*[0-9]+)/$',views.messageApi),
    url(r'^message/([0-9]+)/$',views.messageApi),
]