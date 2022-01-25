import imp
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserRegisterForm


# Create your views here.


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse('accounts:login')
