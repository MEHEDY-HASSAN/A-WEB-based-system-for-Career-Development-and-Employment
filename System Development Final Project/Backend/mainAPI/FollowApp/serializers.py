from rest_framework import serializers
from FollowApp.models import Follow, Active

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('FollowID'
                    )

class ActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Active
        fields = ('ProfileID',
                  'ActiveTime')

