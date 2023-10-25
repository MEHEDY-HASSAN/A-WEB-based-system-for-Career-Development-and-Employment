from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from datetime import datetime
# Create your views here.
from FollowApp.models import Follow, Active
from FollowApp.serializers import FollowSerializer, ActiveSerializer


from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
message_dir  = os.path.join(BASE_DIR,"follow")

@csrf_exempt
def followApi(request,sender,receiver=0):
    
    if request.method=='GET':
        product_list=[]
        try:
            with open (message_dir+"\k"+str(sender), "r") as myfile:
                data = myfile.read().splitlines()
            for i in data:
                mydict = eval(str(i))
                product_list.append(mydict)
            
        except:
            with open(message_dir+"\k"+str(sender),'a+') as f:
                f.write('')
        return JsonResponse(product_list,safe=False)
    

    elif request.method=='POST':
        with open(message_dir+"\k"+str(sender),'a+') as f:
            f.write(str(receiver)+'\n') 
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='DELETE':
        with open(message_dir+"\k"+str(sender),'w') as f:
                f.write('')
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def activeApi(request,id=0):
    if request.method=='GET':
        actives = Active.objects.all().filter(ProfileID=id)
        actives_serializer = ActiveSerializer(actives, many=True)
        return JsonResponse(actives_serializer.data, safe=False)

    elif request.method=='POST':
        active_data=JSONParser().parse(request)
        active_serializer = ActiveSerializer(data=active_data)
        if active_serializer.is_valid():
            active_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed.",safe=False)
    
    elif request.method=='PUT':
        active_data = JSONParser().parse(request)
        active=Active.objects.get(ProfileID=active_data['ProfileID'])
        active_serializer=ActiveSerializer(active,data=active_data)
        if active_serializer.is_valid():
            active_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        active=Active.objects.get(ProfileID=id)
        active.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
