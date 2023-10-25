from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import datetime

# Create your views here.
from PostApp.models import Post
from PostApp.serializers import PostSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def postApi(request,id=0):
    if request.method=='GET':
        logins = Post.objects.all()
        logins_serializer = PostSerializer(logins, many=True)
        return JsonResponse(logins_serializer.data, safe=False)

    elif request.method=='POST':
        login_data=JSONParser().parse(request)
        department_serializer = PostSerializer(data=login_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("login Successfully!!" , safe=False)
        return JsonResponse("Failed.",safe=False)
    
    elif request.method=='PUT':
        login_data = JSONParser().parse(request)
        login=Post.objects.get(PostID=login_data['PostID'])
        login_serializer=PostSerializer(login,data=login_data)
        if login_serializer.is_valid():
            login_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        login=Post.objects.get(PostID=id)
        login.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
