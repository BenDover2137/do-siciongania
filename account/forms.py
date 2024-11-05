from django import forms
from django.contrib.auth import get_user_model


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