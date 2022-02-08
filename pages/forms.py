from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Myuser
# class Login_form(forms.Form):
#     username=forms.CharField(max_length=20)
#     password=forms.CharField(max_length=20,initial="enter password",widget=forms.PasswordInput) 
class Login_form(forms.ModelForm):
    class Meta:
         model = Myuser
         fields = '__all__'