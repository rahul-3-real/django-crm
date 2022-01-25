from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}
