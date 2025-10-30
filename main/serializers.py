from rest_framework import serializers
from main.models import GroupMessage
from django.shortcuts import get_object_or_404

def parent_structurator(message_id):
    message_get = get_object_or_404(GroupMessage, id = message_id)
    son_messages = message_get.son_message.all()
    context = {
    }
    for message in son_messages:
        # if message.exists(): так не може бути бо це ніби того елементу взагалі не було би
        #     print(message)
        #     context[f"soon{message.id}"] = {
        #         "obj": message,
        #         "id": message.id,
        #         "soons": 
        #     }
        # else:
        #     id = message.id
        #     parent_structurator(message_id=id)

        print(message)
        context[f"soon{message.id}"] = {
            "obj": message,
            "id": message.id,
            "soons": parent_structurator(message_id=message.id)
        }
    return context

def structurator(group_id):   
    parent_message = GroupMessage.objects.filter(group__id = group_id, parent__isnull=True)
    parent_iter = iter(parent_message)
    messages = {
    }
    while True:
        try:
            id_message = next(parent_iter)
            messages[f'{id_message.id}'] = {
                'obj': get_object_or_404(GroupMessage, id = id_message.id),
                "soons": parent_structurator(message_id = id_message.id),
            }
        except StopIteration:
            break
        
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