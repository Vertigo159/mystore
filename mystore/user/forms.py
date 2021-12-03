from django import forms
from .models import CustomUser
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.password_validation import validate_password
import re


class UserRegForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'phone', 'email')


    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            self.add_error('password2','Пароли не совпадают.')
        email = self.cleaned_data.get('email')  
        username = self.cleaned_data.get('username')
        if email and CustomUser.objects.filter(email=email).exclude(username=username).exists():
            self.add_error('email', 'Указанный электронный адрес уже существует')
        phone = self.cleaned_data.get('phone')
        if phone and CustomUser.objects.filter(phone=phone).exclude(username=username).exists():
            self.add_error('phone', 'Этот мобильный номер уже существует')
        return super().clean()

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password, self.instance)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password

class LoginForm(forms.Form):

    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)