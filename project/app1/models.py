from django.db import models

# Create your models here.
class class1(models.Model):
    image=models.ImageField(upload_to='pics/justin')
    title=models.CharField(max_length=250)
    desc=models.TextField()