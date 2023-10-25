from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.
from MessageApp.models import Message
from MessageApp.serializers import MessageSerializer

from django.core.files.storage import default_storage

from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
message_dir  = os.path.join(BASE_DIR,"message")

@csrf_exempt
def messageApi(request,sender=0,receiver= 0):
    
    if request.method=='GET' and receiver==0:
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
    
    elif request.method=='GET' and receiver=="-2":
        product_list=[]
        vis={}
        c = 1;
        try:
            with open (message_dir+"\k"+str(sender)+"all", "r") as myfile:
                data = myfile.read().splitlines()
            for i in data:
                mydict = eval(str(i))
                if (mydict['MessageSenderID']==int(sender)):
                    vis[mydict['MessageReceiverID']] = c 
                    c = c+1
                    product_list.append(mydict)
                else :
                    vis[mydict['MessageSenderID']] = c 
                    c = c+1
                    product_list.append(mydict)
            
            final_product_list=[]
            for index, item in enumerate(product_list): 
                if (item['MessageSenderID']==int(sender)):
                    if (vis[item['MessageReceiverID']]==index+1):
                        final_product_list.append(item)
                else :
                    if (vis[item['MessageSenderID']]==index+1):
                        final_product_list.append(item)

            product_list = final_product_list
            
                 
        except:
            with open(message_dir+"\k"+str(sender)+"all",'a+') as f:
                f.write('')
        return JsonResponse(product_list,safe=False)

    elif request.method=='GET':
        
        product_list=[]
        try:
            with open (message_dir+"\k"+str(sender)+"_"+str(receiver), "r") as myfile:
                data = myfile.read().splitlines()
            for i in data:
                mydict = eval(str(i))
                product_list.append(mydict)
        except:
            with open(message_dir+"\k"+str(sender)+"_"+str(receiver),'a+') as f:
                f.write('')
        return JsonResponse(product_list,safe=False)

    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer = MessageSerializer(data=department_data)
        if department_serializer.is_valid():

            with open(message_dir+"\k"+str(sender)+"_"+str(receiver),'a+') as f:
                f.write(str(department_serializer.initial_data)+'\n')
            with open(message_dir+"\k"+str(sender)+"all",'a+') as f:
                f.write(str(department_serializer.initial_data)+'\n')
            with open(message_dir+"\k"+str(receiver)+"_"+str(sender),'a+') as f:
                f.write(str(department_serializer.initial_data)+'\n')
            with open(message_dir+"\k"+str(receiver)+"all",'a+') as f:
                f.write(str(department_serializer.initial_data)+'\n')
            with open(message_dir+"\k"+str(receiver),'a+') as f:
                f.write(str(sender)+'\n') 

            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='DELETE':
        with open(message_dir+"\k"+str(sender),'w') as f:
                f.write('')
        return JsonResponse("Deleted Succeffully!!", safe=False)