from django.forms import ModelForm
from django import forms
from .models import Contact
from django.contrib.auth.models import User

class AddContactForm(ModelForm):
    values = User.objects.all().values()
    user = forms.Select(choices=values)
    # users = User.objects.all().values_list('username', flat=True)
    # choices = [('None', 'None')] + [(username, username) for username in users]
    # default_username = None
    # user = forms.ChoiceField(choices=choices, initial=None, widget=forms.Select, required=False)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=False, max_length=30)
    image = forms.ImageField(required=False)
    email = forms.EmailField(required=False, max_length=50)
    phone = forms.CharField(required=False, max_length=10)
    mobile = forms.CharField(required=False, max_length=11)
    address = forms.CharField(required=False, max_length=30)
    nickname = forms.CharField(required=False, max_length=30)
    class Meta:
        model = Contact
        fields = ['user', 'first_name', 'last_name', 'image', 'email', 'phone', 'mobile', 'address', 'nickname']