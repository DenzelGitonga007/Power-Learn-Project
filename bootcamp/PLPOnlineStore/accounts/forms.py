from django import forms
from django.contrib.auth.form import UserCreationForm
from django.contrib.auth.models import User


class CustomerSignUpForm(UserCreationForm):
    # Field inputs
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_lenght=100, required=True)
    email = forms.EmailField(max_length=250, help_text='e.g youremail@gmail.com')

    # To order/sort data
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')