from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.


class User(AbstractUser):

    STARTAPPER = 'startapper'
    DEVELOPER = 'developer'
    PRACTITIONER = 'practitioner'

    USER_TYPE = [
        (STARTAPPER , 'startapper'),
        (DEVELOPER , 'developer'),
        (PRACTITIONER , 'practitioner'),
    ]

    fullname  = models.CharField('full_name', max_length='100' , null=True )
    email = models.EmailField('email' , unique=True)   
    phone = models.CharField('phone' , max_length=20 , unique=True)
    user_type = models.CharField('User_Type' , choices=USER_TYPE)
    date_joined = models.DateField('Date_Joined' , auto_now_add=True)


class Startapper(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to='Startapp_project/%Y/%m/%d/')
    description=models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ("Startapper")
        verbose_name_plural = ("Startappers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Startapp_detail", kwargs={"pk": self.pk})
    
    
class Programmer(models.Model):
    BACKEND = 'backend'
    FRONTEND = 'frontedn'
    MOBILE = 'mobile'

    DIRECTION = [
        (BACKEND , 'backend'),
        (FRONTEND , 'frontedn'),
        (MOBILE , 'mobile'),
    ]

    user = models.OneToOneField(User , on_delete=models.CASCADE)
    information=models.TextField()
    direction = models.CharField(choices=DIRECTION , default=BACKEND)
    resume = models.FileField(upload_to='stuff_resume/%Y/%m/%d/')

    class Meta:
        verbose_name = ("Developer")
        verbose_name_plural = ("Developers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Developer_detail", kwargs={"pk": self.pk})

