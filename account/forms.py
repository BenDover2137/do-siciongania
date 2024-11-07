from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm

from account.models import Profile


class LoginForm(forms.Form):
    username=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput, label='Haslo')
    password1 = forms.CharField(widget=forms.PasswordInput, label='powtoz haslo')
    class Meta:
        model=get_user_model()
        fields=['username','first_name','email']
    def clean_passsword2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError('hasla nie takie same')
class UserEditForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=['first_name','last_name','email']
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['date_of_birth','photo']