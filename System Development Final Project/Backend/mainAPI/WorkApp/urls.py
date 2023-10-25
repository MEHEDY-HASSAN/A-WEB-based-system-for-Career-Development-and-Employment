from django.urls import re_path as url
from WorkApp import views


urlpatterns=[
    url(r'^work/$',views.workApi),
    url(r'^work/([0-9]+)$',views.workApi),
    
    url(r'^category/$',views.categoryApi),
    url(r'^category/([0-9]+)$',views.categoryApi),
]