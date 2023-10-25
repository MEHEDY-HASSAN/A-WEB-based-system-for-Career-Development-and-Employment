from rest_framework import serializers
from MessageApp.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('MessageSenderID',
                  'MessageReceiverID',
                  'Message',
                  'MessageSenderName',
                  'MessageReceiverName',
                  'MessageSenderProfilePicture',
                  'MessageReceiverProfilePicture',
                  'MessageSendDateTime')