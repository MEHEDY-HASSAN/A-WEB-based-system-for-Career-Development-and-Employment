from rest_framework import serializers
from AboutApp.models import About

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('ProfileID',
                  'Phone',
                  'Profession',
                  'Location',
                  'Gender',
                  'skill')