from rest_framework import serializers
from main.models import GroupMessage, Post
from django.shortcuts import get_object_or_404

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


def parent_structurator(message_id):
    message_get = get_object_or_404(GroupMessage, id = message_id)
    son_messages = message_get.son_message.all()
    context = {
    }
    for message in son_messages:
        print(message)
        context[f"soon{message.id}"] = {
            "obj": message.message,
            "id": message.id,
            'user': message.user.email,
            "soons": parent_structurator(message_id=message.id)
        }
    return context

def structurator(group_id):   
    parent_messages = GroupMessage.objects.filter(group__id = group_id, parent__isnull=True)
    messages = {
    }
    for parent_message in parent_messages:
        messages[f'{parent_message.id}'] = {
            'obj': parent_message.message,
            'id': parent_message.id,
            'user': parent_message.user.email,
            "soons": parent_structurator(message_id = parent_message.id),
        }
 
    context = {
        "group_id":group_id,
        "messages":messages,
    }
    return context




class GroupMessageSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source = 'user.email', read_only=True)
    class Meta:
        model = GroupMessage
        fields = ['user_email','date','message','file']