from rest_framework import serializers
from main.models import GroupMessage, Post, MediaPost
from django.shortcuts import get_object_or_404
class MediaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaPost
        fields = ['media']

class PostSerializer(serializers.ModelSerializer):
    profile_user_email = serializers.CharField(source = 'profile.user.email', read_only=True)
    profile_avatar = serializers.CharField(source = 'profile.avatar', read_only=True)
    media = MediaPostSerializer(many=True, read_only=True, source='media_posts')
    class Meta:
        model = Post
        fields = ['parent','profile_user_email','profile_avatar','description','date_publish','id','media']#,'media'


def parent_structurator(message_id):
    message_get = get_object_or_404(GroupMessage, id = message_id)
    son_messages = message_get.son_message.all()
    context = {
    }
    for message in son_messages:
        print(message)
        context[f"soon{message.id}"] = {
            'obj': message.message,
            'id': message.id,
            'user': message.user.email,
            'soons': parent_structurator(message_id=message.id)
        }
    return context

def structurator(group_id, type):   
    parent_messages = GroupMessage.objects.filter(group__id = group_id, parent__isnull=True)
    messages = {
    }
    for parent_message in parent_messages:
        messages[f'{parent_message.id}'] = {
            'obj': parent_message.message,
            'id': parent_message.id,
            'user': parent_message.user.email,
            'soons': parent_structurator(message_id = parent_message.id),
        }
 
    context = {
        "type":type,
        "group_id":group_id,
        "messages":messages,
    }
    return context




class GroupMessageSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source = 'user.email', read_only=True)
   ##custom func
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    parent = serializers.SerializerMethodField()
    class Meta:
        model = GroupMessage 
        fields = ['parent','id','user_email','date','message','file']

    def get_parent(self, obj):
        message = obj.parent
        if message == None:
            message = None
        else:
            message = obj.parent.message
        return message