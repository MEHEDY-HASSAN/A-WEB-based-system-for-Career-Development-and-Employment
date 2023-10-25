from rest_framework import serializers
from ProfileApp.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('ProfileID',
                  'ProfileName',
                  'ProfilePicture',
                  'ProfileCoverPhoto',
                  'ProfileBio')