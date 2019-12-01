from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    date_created = models.DateField()

    def __str__(self):
        return self.name

class Languages(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=20)
    paradigm = models.CharField(max_length=20)
    date_created = models.DateField()

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age=models.IntegerField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    languages = models.ManyToManyField(Languages)

    def __str__(self):
        return self.name

