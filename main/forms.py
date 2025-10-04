from django import forms
from .models import Post, Post_reaction, Group, Group_message, Group_Reaction_message, Group_users, Profile
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateInput
from main.models import Profile

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })
    class Meta:
        model = Profile
        fields = ['biography','avatar','cover']
