from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label='Логин для входа')
    first_name = forms.CharField(max_length=30, required=True, label='Имя')
    last_name = forms.CharField(max_length=30, required=True, label='Фамилия')
    email = forms.CharField(max_length=30, required=True, label='email')
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Повторите пароль')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')