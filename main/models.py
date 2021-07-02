from os import name
from django.db import models
from django.urls import reverse
# Create your models here.
class Startapper(models.Model):
    name=models.CharField(max_length=100)
    video=models.FileField(upload_to='media')
    audio=models.FileField(blank=True,upload_to='media')
    pdf=models.FileField(upload_to='documents/%Y/%m/%d/')
    document=models.FileField(upload_to='documents/%Y/%m/%d/')
    description=models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ("Startapper")
        verbose_name_plural = ("Startappers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Startapp_detail", kwargs={"pk": self.pk})
    
    
class Developer(models.Model):
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="developers")
    age=models.IntegerField()
    description=models.TextField()
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=30)
    
    class Meta:
        verbose_name = ("Developer")
        verbose_name_plural = ("Developers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Developer_detail", kwargs={"pk": self.pk})
