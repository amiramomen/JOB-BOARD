from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'password1', 'password2', 'email']



class Userform (forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name' , 'email']

class Profileform (forms.ModelForm):
    class Meta:
        model = Profile
        fields =['phone', 'image','city']
        