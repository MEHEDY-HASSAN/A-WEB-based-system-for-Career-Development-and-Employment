from rest_framework import serializers
from LoginApp.models import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('loginID',
                  'EmailAddress',
                  'Password')