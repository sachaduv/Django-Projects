from django.db import models

class Todo(models.Model):
    task=models.CharField(max_length=40)
    complete= models.BooleanField(default=False)
