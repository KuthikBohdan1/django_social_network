from rest_framework import serializers
from main.models import GroupMessage
from django.shortcuts import get_object_or_404

# def parent_structurator(message_id):
#     message_get = get_object_or_404(GroupMessage, id = message_id)
#     son_messages = message_get.son_message.all()
#     context = {
#     }
#     for message in son_messages:
#         print(message)
#         context[f"soon{message.id}"] = {
#             "obj": message.message,
#             "id": message.id,
#             "soons": parent_structurator(message_id=message.id)
#         }
#     return context

# def structurator(group_id):   
#     parent_messages = GroupMessage.objects.filter(group__id = group_id, parent__isnull=True)
#     messages = {
#     }
    # for parent_message in parent_messages:
    #     messages[f'{parent_message.id}'] = {
    #         'obj': parent_message,
    #         "soons": parent_structurator(message_id = parent_message.id),
    #     }
 
    # context = {
    #     "group_id":group_id,
    #     "messages":messages,
    # }
    # return context


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
    parent_messages = GroupMessage.objects.filter(group__id = group_id, parent__isnull=True)
    # parent_iter = iter(parent_message)
    messages = {
    }
    for parent_message in parent_messages:
        messages[f'{parent_message.id}'] = {
            'obj': get_object_or_404(GroupMessage, id = parent_message.id),
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