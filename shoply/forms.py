from django import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        "placeholder": 'username@domain.tld'
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "placeholder": 'verysecurepassword'
    }))


class RegisterForm(forms.Form):

    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={
        "placeholder": 'user123'
    }))

    first_name = forms.CharField(label="First name", widget=forms.TextInput(attrs={
        "placeholder": 'Victor'
    }))

    last_name = forms.CharField(label="Last name", widget=forms.TextInput(attrs={
        "placeholder": 'Poulton'
    }))

    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        "placeholder": 'username@domain.com'
    }))

    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "placeholder": 'verysecurepassword'
    }))

    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={
        "placeholder": 'verysecurepassword'
    }))


    def clean(self):
        data = self.cleaned_data
        username = User.objects.filter(username=data.get('username'))
        email = User.objects.filter(email=data.get('email'))

        if len(data['password']) < 6:
            raise forms.ValidationError("password is too short")


        if len(username) > 0:
            raise forms.ValidationError("username is already taken")


        if len(email) > 0:
            raise forms.ValidationError("email is already being used")

        print(data)
        return data


    def register(self):
        print("register", self.cleaned_data)

        

        return redirect(to="/login")