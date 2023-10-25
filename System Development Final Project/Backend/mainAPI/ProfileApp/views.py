from sqlite3 import Date
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import datetime

# Create your views here.

from ProfileApp.models import Profile
from ProfileApp.serializers import ProfileSerializer
#for image saving in server
from django.core.files.storage import default_storage

@csrf_exempt
def ProfileApi(request,id=0):
    if request.method=='GET' and id==0:
        profiles = Profile.objects.all()
        profiles_serializer = ProfileSerializer(profiles, many=True)
        return JsonResponse(profiles_serializer.data, safe=False)

    elif request.method=='GET':
        profiles = Profile.objects.all().filter(ProfileID = id)
        profiles_serializer = ProfileSerializer(profiles, many=True)
        lis = list(profiles_serializer.data)
        c = 0
        for i in lis:
            c = c+1
        if (c>0) :
            return JsonResponse(profiles_serializer.data, safe=False)
        else : return JsonResponse("false",safe=False)

    elif request.method=='POST':
        profile_data=JSONParser().parse(request)
        profile_serializer = ProfileSerializer(data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse("login Successfully!!" , safe=False)
        return JsonResponse("Failed.",safe=False)
    
    elif request.method=='PUT':
        profile_data = JSONParser().parse(request)
        profile=Profile.objects.get(ProfileID=profile_data['ProfileID'])
        profile_serializer=ProfileSerializer(profile,data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        profile=Profile.objects.get(ProfileID=id)
        profile.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def SaveFile(request):
    if request.method=='POST':
        file=request.FILES['uploadedFile']
        date_time = datetime.datetime.now()
        dt_string = date_time.strftime("%d_%m_%Y_%H_%M_%S") + file.name
        file_name = default_storage.save(dt_string,file)
        return JsonResponse(file_name,safe=False)