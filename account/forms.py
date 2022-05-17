from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from users.models import CustomUser
from django import forms
import re


class CreateUserForm(UserCreationForm):
    GENDORS = (

        ('M', 'MEN'),
        ('F', 'WOME'),

    )

    gender = forms.ChoiceField(choices=GENDORS)


    class Meta:
        model = CustomUser

        fields = ['username','email','password1','gender']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password verification'


    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.email_tag = re.split(r'@', instance.email)[1]
        if commit:
            instance.save()
            self.save_m2m()
        return instance

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'email_tag','gender']





