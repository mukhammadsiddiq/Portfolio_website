from django.db import models
from django.urls import reverse


# Create your models here.
class ProfileInfo(models.Model):
    title = models.CharField(max_length=120)
    profile = models.TextField()
    address = models.CharField(max_length=120)
    image = models.ImageField(upload_to='personal/')
    resume = models.FileField(upload_to='files/')
    year_experience = models.CharField(max_length=120, default='2+')
    instagram = models.CharField(max_length=120, default='https://instagram.com/ibroximov_m_')
    telegram = models.CharField(max_length=120, default='https://t.me/IbrokhimovMukhammad')
    linkedin = models.CharField(max_length=120, default='https://www.linkedin.com/in/ibroximov')
    github = models.CharField(max_length=120, default='https://github.com/mukhammadsiddiq')

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


class JobInfo(models.Model):
    title = models.CharField(max_length=200)
    Upper_title = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    website =models.CharField(max_length=200)
    body1 = models.TextField()
    body2 = models.TextField()
    body3 = models.TextField()
    body4 = models.TextField()
    body5 = models.TextField()
    information = models.TextField()
    image = models.ImageField(upload_to="personal/")

    def __str__(self):
        return self.title


class PartTime(models.Model):
    title = models.CharField(max_length=200, default="Fill the form")
    data = models.CharField(max_length=200, default="Fill the form")
    address = models.CharField(max_length=200, default="Fill the form")
    company = models.CharField(max_length=200, default="Fill the form")
    website = models.CharField(max_length=200, default="Fill the form")
    information = models.TextField(default="Fill the form")
    body = models.TextField(default="Fill the form")
    image = models.ImageField(upload_to="personal/", default="Fill the form")

    def __str__(self):
        return self.title

