from django.contrib import admin
from main.models import Profile, Post, PostReaction, CommentPost, Group, GroupMessage, GroupUser, GroupReactionMessage

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(PostReaction)
admin.site.register(CommentPost)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name','type','description')
    search_fields = ('name',)
    list_filter = ('name',)

fieldsets = (
    ('головна ',
        {
            'fields': ('name','creator__email')
        },
    ),
    
)

class GroupUserInline(admin.TabularInline):
    model = GroupUser
    
admin.site.register(GroupMessage)
admin.site.register(GroupUser)
admin.site.register(GroupReactionMessage)



# Register your models here.
