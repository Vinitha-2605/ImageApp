from django import forms
from .models import Login, Register

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'