from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import datetime

# Create your views here.
from WorkApp.models import Work , Catagory
from WorkApp.serializers import WorkSerializer , CategorySerializer

from django.core.files.storage import default_storage

@csrf_exempt
def workApi(request,id=0):
    if request.method=='GET':
        logins = Work.objects.all()
        logins_serializer = WorkSerializer(logins, many=True)
        return JsonResponse(logins_serializer.data, safe=False)

    elif request.method=='POST':
        login_data=JSONParser().parse(request)
        department_serializer = WorkSerializer(data=login_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("login Successfully!!" , safe=False)
        return JsonResponse("Failed.",safe=False)
    
    elif request.method=='PUT':
        login_data = JSONParser().parse(request)
        login=Work.objects.get(WorkID=login_data['WorkID'])
        login_serializer=WorkSerializer(login,data=login_data)
        if login_serializer.is_valid():
            login_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        login=Work.objects.get(WorkID=id)
        login.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def categoryApi(request,id=0):
    if request.method=='GET':
        logins = Catagory.objects.all()
        logins_serializer = CategorySerializer(logins, many=True)
        return JsonResponse(logins_serializer.data, safe=False)

    elif request.method=='POST':
        login_data=JSONParser().parse(request)
        department_serializer = CategorySerializer(data=login_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("login Successfully!!" , safe=False)
        return JsonResponse("Failed.",safe=False)
    
    elif request.method=='PUT':
        login_data = JSONParser().parse(request)
        login=Catagory.objects.get(CatID=login_data['CatID'])
        login_serializer=CategorySerializer(login,data=login_data)
        if login_serializer.is_valid():
            login_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        login=Catagory.objects.get(CatID=id)
        login.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
