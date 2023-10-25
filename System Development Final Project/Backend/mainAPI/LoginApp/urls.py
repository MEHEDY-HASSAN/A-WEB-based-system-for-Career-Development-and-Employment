from django.urls import re_path as url
from LoginApp import views

urlpatterns=[
    url(r'^login/$',views.loginApi),
    url(r'^login/([0-9]+)$',views.loginApi),
]