from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import datetime

# Create your views here.
from StoryApp.models import Story
from StoryApp.serializers import StorySerializer

from django.core.files.storage import default_storage

@csrf_exempt
def storyApi(request,id=0):
    if request.method=='GET':
        logins = Story.objects.all()
        logins_serializer = StorySerializer(logins, many=True)
        return JsonResponse(logins_serializer.data, safe=False)

    elif request.method=='POST':
        login_data=JSONParser().parse(request)
        department_serializer = StorySerializer(data=login_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("login Successfully!!" , safe=False)
        return JsonResponse("Failed.",safe=False)
    
    elif request.method=='PUT':
        login_data = JSONParser().parse(request)
        login=Story.objects.get(StoryID=login_data['StoryID'])
        login_serializer=StorySerializer(login,data=login_data)
        if login_serializer.is_valid():
            login_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        login=Story.objects.get(StoryID=id)
        login.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
