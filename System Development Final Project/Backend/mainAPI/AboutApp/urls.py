from django.urls import re_path as url
from AboutApp import views

urlpatterns=[
    url(r'^about/$',views.aboutApi),
    url(r'^about/([0-9]+)$',views.aboutApi),
]