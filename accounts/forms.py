from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser


class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email']


class LoginForm(AuthenticationForm):######якщо стоврюєш кастомну реістрію використовуй та наслідуй від AuthenticationForm щоб перевіряти 
    #чи залогінений користувач та передавати в реквест get_user без цього працювати не буде та буде  AttributeError at /login/'LoginForm' object has no attribute 'get_user'
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None) 
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })

    # class Meta:
    #     model = CustomUser
    #     fields = ['email','password']

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })


# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })

#         self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2'})
#         self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2'})