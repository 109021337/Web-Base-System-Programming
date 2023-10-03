from django import forms
from captcha.fields import CaptchaField
from django.forms import widgets


class PostForm(forms.Form):
    username = forms.CharField(max_length=20,initial='')
    pd = forms.CharField(widget=widgets.PasswordInput,max_length=20, initial='')
    captcha = CaptchaField()
