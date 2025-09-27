from django.contrib import admin
from main.models import CustomUser, Post, Post_like, Coment_Post

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Post_like)
admin.site.register(Coment_Post)
admin.site.register()
# Register your models here.
