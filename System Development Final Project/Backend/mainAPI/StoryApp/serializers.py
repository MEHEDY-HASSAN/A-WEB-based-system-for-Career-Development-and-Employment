from rest_framework import serializers
from StoryApp.models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('StoryID',
                  'ProfileID',
                  'ProfileName',
                  'ProfilePicture',
                  'StoryDate',
                  'StoryImage')