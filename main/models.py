from django.db import models
from accounts.models import CustomUser


class Profile(models.Model):
    # name = models.CharField(max_length=125, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    biography = models.TextField(null=True, blank=True, default="no bio yet")
    avatar = models.ImageField(upload_to="profiles/avatars/", null=True, blank=True)
    cover = models.ImageField(upload_to="profiles/covers/", null=True, blank=True)
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    ##########################33
    parent = models.ForeignKey("Post", on_delete=models.CASCADE, null=True, blank=True)
    ####################333333
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')#profile.posts всі пости на профілі
    description = models.TextField(null=True, blank=True)
    date_publish = models.DateTimeField(auto_now_add=True)
    like_fast = models.IntegerField(default= 0)
    # media = models.ForeignKey(MediaPost,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.parent} / {self.description}"
    
class MediaPost(models.Model):
    media = models.FileField(upload_to="media_posts/")
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media_posts')## post.media_posts.all
    def __str__(self):
        return f"{self.post} / {self.media}"
    
class PostReaction(models.Model):
    REACTION_CHOICES = (
        ('like','👍'),
        ('dislike','👎'),
        ('funny','😂'),
        ('sad','😢'),
    )
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reactions") # post.reactions.all ніби всі реакції поста
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reactions')# user.reactions.all ніби як всі реакцї юзера
    def __str__(self):
        return f"post/parent|{self.post}| / {self.user.user_nikname} / {self.reaction} "
    
    class Meta:
        unique_together = [['user', 'post']]

class CommentPost(models.Model):
    #############################
    parent = models.ForeignKey("CommentPost", on_delete=models.CASCADE, null=True, blank=True, related_name="replits") ###ніюи як відповіді 
    #########################
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="comments") #user.posts.all
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")# post.comment.all
    text = models.TextField(null=True, blank=True)
    media = models.FileField(upload_to="coment_posts/", null=True, blank=True)
    date_publish = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.text} / {self.author}"

class Group(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField(default="no description group")
    image_group = models.ImageField(upload_to="groups/image_groups/", null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
    
class GroupUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_groups")### user.group.all всі групи користувача потім в пенелі з чатами тре буде використовувати
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_users")# на сторінці чату виуодить список користувачів в групі
    def __str__(self):
        return f"{self.user} / {self.group}"
    
class GroupMessage(models.Model):
    parent = models.ForeignKey("GroupMessage", on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file  = models.FileField(null=True, blank=True, upload_to="group_message/")
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.parent} / {self.message}"

class GroupReactionMessage(models.Model):
    REACTION_CHOICES = (
        ('like','👍'),
        ('dislike','👎'),
        ('funny','😂'),
        ('sad','😢'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reaction = models.CharField(choices=REACTION_CHOICES)
    Group_message = models.ForeignKey(GroupMessage, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} / {self.reaction}"
     
    class Meta:
        unique_together = [['user']]