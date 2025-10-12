from django import forms
from .models import Post, MediaPost, PostReaction, Group, GroupMessage, GroupReactionMessage, GroupUser, Profile
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateInput, ImageField, FileField, ClearableFileInput
from main.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biography','avatar']###'cover'
        widgets = {
            'biography': TextInput(),

        }

class PostForm(forms.ModelForm):
    # media = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    class Meta:
        model = Post
        fields = ['parent','text','description']
        widgets = {
        }

# class MediaPostForm(forms.ModelForm):
#     class Meta:
#         model = MediaPost
#         fields = ['media']
#         widgets = {
#             'media': ClearableFileInput(),
#         }