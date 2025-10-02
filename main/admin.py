from django.contrib import admin
from main.models import Profile, Post, Post_reaction, Comment_Post, Group, Group_message, Group_users, Group_Reaction_message

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Post_reaction)
admin.site.register(Comment_Post)
admin.site.register(Group)
admin.site.register(Group_message)
admin.site.register(Group_users)
admin.site.register(Group_Reaction_message)

# Register your models here.
