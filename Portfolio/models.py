from django.db import models
from django.urls import reverse


# Create your models here.
class ProfileInfo(models.Model):
    title = models.CharField(max_length=120)
    profile = models.TextField()
    address = models.CharField(max_length=120)
    image = models.ImageField(upload_to='personal/')
    resume = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title


class EducationInfo(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    website =models.CharField(max_length=200)
    body = models.TextField()
    information = models.TextField()
    image = models.ImageField(upload_to="personal/")

    def __str__(self):
        return self.title
