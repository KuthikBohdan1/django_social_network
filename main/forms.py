from django import forms
from .models import Post, Post_reaction, Group, Group_message, Group_Reaction_message, Group_users, Profile
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateInput, ImageField, FileField
from main.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biography','avatar']###'cover'
        widgets = {
            'biography': TextInput(),

        }
