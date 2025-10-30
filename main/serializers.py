from rest_framework import serializers
from main.models import GroupMessage

class GroupMessageSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source = 'user.email', read_only=True)
    class Meta:
        model = GroupMessage
        fields = ['user_email','date','message','file']