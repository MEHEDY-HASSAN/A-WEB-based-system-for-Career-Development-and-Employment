from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


# Create your views here.
from AboutApp.models import About
from AboutApp.serializers import AboutSerializer

@csrf_exempt
def aboutApi(request,id=0):
    if request.method=='GET' and id!=0:
        abouts = About.objects.all().filter(ProfileID=id)
        abouts_serializer = AboutSerializer(abouts, many=True)
        return JsonResponse(abouts_serializer.data, safe=False)

    elif request.method=='POST':
        about_data=JSONParser().parse(request)
        department_serializer = AboutSerializer(data=about_data)
        print(department_serializer)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed.",safe=False)
    
    elif request.method=='PUT':
        about_data = JSONParser().parse(request)
        about=About.objects.get(ProfileID=about_data['ProfileID'])
        about_serializer=AboutSerializer(about,data=about_data)
        if about_serializer.is_valid():
            about_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        about=About.objects.get(ProfileID=id)
        about.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
