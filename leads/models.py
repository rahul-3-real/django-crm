from django.db import models
from accounts.models import Agent, UserProfile

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Lead(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    age = models.IntegerField(default=0)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey(
        Agent, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='leads')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
