from django.contrib import admin
from main.models import Profile, Post, PostReaction, CommentPost, Group, GroupMessage, GroupUser, GroupReactionMessage

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(PostReaction)
admin.site.register(CommentPost)
admin.site.register(Group)
admin.site.register(GroupMessage)
admin.site.register(GroupUser)
admin.site.register(GroupReactionMessage)

# Register your models here.
