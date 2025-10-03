from django.db import models
from accounts.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    biography = models.TextField(null=True, blank=True, default="no bio yet")
    avatar = models.ImageField(upload_to="profile/avatar/", null=True, blank=True)
    cover = models.ImageField(upload_to="profile/cover/", null=True, blank=True)
    def __str__(self):
        return self.user.user_nikname

class Post(models.Model):
    ##########################33
    parent = models.ForeignKey("Post", on_delete=models.CASCADE, null=True, blank=True)
    ####################333333
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')#profile.posts всі пости на профілі
    text = models.CharField(max_length=256)
    description = models.TextField()
    media = models.FileField(upload_to="posts/media/")
    date_publish = models.DateTimeField(auto_now_add=True)
    like_fast = models.IntegerField(default= 0)

class Post_reaction(models.Model):
    REACTION_CHOICES = (
        ('like','👍'),
        ('dislike','👎'),
        ('funny','😂'),
    )
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reactions") # post.reactions.all ніби всі реакції поста
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reactions')# user.reactions.all ніби як всі реакцї юзера
    def __str__(self):
        return self.like
    
    class Meta:
        unique_together = [['user', 'post']]

class Comment_Post(models.Model):
    #############################
    parent = models.ForeignKey("Comment_Post", on_delete=models.CASCADE, null=True, blank=True, related_name="replits") ###ніюи як відповіді 
    #########################
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="comments") #user.posts.all
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")# post.comment.all
    text = models.TextField()
    media = models.FileField(upload_to="coment_post/", null=True, blank=True)
    date_publish = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image_goroup = models.ImageField(upload_to="Group/image_group/", null=True, blank=True)

class Group_users(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_groups")### user.group.all всі групи користувача потім в пенелі з чатами тре буде використовувати
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_users")# на сторінці чату виуодить список користувачів в групі

class Group_message(models.Model):
    parent = models.ForeignKey("Group_message", on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file  = models.FileField(null=True, blank=True, upload_to="Group_message_file/")
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Group_Reaction_message(models.Model):
    REACTION_CHOICES = (
        ('like','👍'),
        ('dislike','👎'),
        ('funny','😂'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reaction = models.CharField(choices=REACTION_CHOICES)
    Group_message = models.ForeignKey(Group_message, on_delete=models.CASCADE)
    class Meta:
        unique_together = [['user']]
