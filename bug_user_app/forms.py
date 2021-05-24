'''
    User Forms for login
'''

from django import forms
from bug_user_app.models import CustomUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password'
        ]