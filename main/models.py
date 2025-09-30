from django.db import models
from accounts.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    biography = models.CharField(max_length=650, null=True, blank=True, default="no bio yet")
    avatar = models.ImageField(upload_to="profile/avatar/", null=True, blank=True)
    cover = models.ImageField(upload_to="profile/cover/", null=True, blank=True)

class Post(models.Model):
    ##########################33
    parent = models.ForeignKey("Post", null=True, blank=True)
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
    reaction = models.CharField(max_length=3, choices=REACTION_CHOICES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reactions") # post.reactions.all ніби всі реакції поста
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reactions')# user.reactions.all ніби як всі реакцї юзера
    def __str__(self):
        return self.like
    
    class Meta:
        unique_together = [['user', 'post']]

class Comment_Post(models.Model):
    #############################
    parent = models.ForeignKey("Coment_Post", null=True, blank=True, related_name="replits") ###ніюи як відповіді 
    #########################
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="comments") #user.posts.all
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")# post.comment.all
    text = models.TextField()
    media = models.FileField(upload_to="coment_post/", null=True, blank=True)
    date_publish = models.DateTimeField(auto_now_add=True)

