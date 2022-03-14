from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile

class UserRegistration(UserCreationForm):
    email = forms.EmailField(label="Email :", widget=forms.EmailInput(
        attrs={'placeholder': 'Enter Email'}))
    username = forms.CharField(label="Username :", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Username'}))
    password1 = forms.CharField(label="Password : ", required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password'}))

    password2 = forms.CharField(label="Password Confirmation: ", required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Your Password'}))

    class Meta:
        model=User
        fields = ['username', 'email',  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="Email : ")
    username = forms.CharField(label="Username : ")
    class Meta:
        model = User
        fields= ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(label="Image :")
    description = forms.Textarea()

    class Meta:
        model=Profile
        fields=['image','description']