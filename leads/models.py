from django.db import models
from accounts.models import Agent

# Create your models here.


class Lead(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
