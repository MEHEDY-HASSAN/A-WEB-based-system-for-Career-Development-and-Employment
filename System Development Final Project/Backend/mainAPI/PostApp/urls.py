from django.urls import re_path as url
from PostApp import views


urlpatterns=[
    url(r'^post/$',views.postApi),
    url(r'^post/([0-9]+)$',views.postApi),
]