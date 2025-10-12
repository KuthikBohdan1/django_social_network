from django import forms
from .models import Post, Post_reaction, Group, Group_message, Group_Reaction_message, Group_users, Profile, Media_Post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateInput, ImageField, FileField
from main.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biography','avatar']###'cover'
        widgets = {
            'biography': TextInput(),

        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['parent','media','text','description']
        widgets = {
            
        }

class Media_postForm(forms.ModelForm):
    class Meta:
        model = Media_Post