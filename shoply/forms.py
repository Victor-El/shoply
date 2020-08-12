from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        "placeholder": 'username@domain.com'
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "placeholder": 'verysecurepassword'
    }))