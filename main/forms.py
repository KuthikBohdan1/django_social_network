from django import forms
from .models import Post, MediaPost, CommentPost, PostReaction, Group, GroupMessage, GroupReactionMessage, GroupUser, Profile
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateInput, ImageField, FileField, ClearableFileInput
from main.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biography','avatar']
        widgets = {
            'biography': TextInput(),
            
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })

class PostForm(forms.ModelForm):
    # media = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    class Meta:
        model = Post
        fields = ['description']
        widgets = {
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })
class CommentPostForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ['text', 'media']
        
        widgets = {
            'text': TextInput,
            'media': ClearableFileInput,
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })
class GroupMessageForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['message']

        widgets = {
            'message': Textarea(attrs={'class': 'form-control', 'rows': 3} ),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })