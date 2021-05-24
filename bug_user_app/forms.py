'''
    User Forms for login
'''

from django import forms
from bug_user_app.models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)