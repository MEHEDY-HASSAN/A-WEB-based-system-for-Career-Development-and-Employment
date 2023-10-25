from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Create your views here.
from LoginApp.models import Login
from LoginApp.serializers import LoginSerializer

@csrf_exempt
def loginApi(request,id=0):
    if request.method=='GET':
        logins = Login.objects.all()
        logins_serializer = LoginSerializer(logins, many=True)
        return JsonResponse(logins_serializer.data, safe=False)

    elif request.method=='POST':
        login_data=JSONParser().parse(request)
        department_serializer = LoginSerializer(data=login_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("login Successfully!!" , safe=False)
        return JsonResponse("Failed.",safe=False)
    
    elif request.method=='PUT':
        login_data = JSONParser().parse(request)
        login=Login.objects.get(loginID=login_data['loginID'])
        login_serializer=LoginSerializer(login,data=login_data)
        if login_serializer.is_valid():
            login_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        login=Login.objects.get(loginID=id)
        login.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
