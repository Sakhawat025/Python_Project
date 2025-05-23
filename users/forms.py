from django import forms
from .models import CustomUser
from myapp.models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'phone', 'address', 'profile_picture']


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    image = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'password', 'image']  # add 'image'