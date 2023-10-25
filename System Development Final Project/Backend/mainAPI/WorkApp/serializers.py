from rest_framework import serializers
from WorkApp.models import  Work , Catagory

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('WorkID',
                  'ProfileID',
                  'ProfileName',
                  'ProfilePicture',
                  'ProfileRating',
                  'WorkTittle',
                  'WorkPicture',
                  'WorkRating',
                  'WorkReview',
                  'StartingMoney',
                  'WorkSummery',
                  'WorkDetails',
                  'WorkCatagory',
                  'workSubCatagory')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = ('CatID',
                  'CatSub')