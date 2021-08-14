from django.db import models

# Create your models here.
class HelloWorld(models.Model):   #Model상속
    text = models.CharField(max_length=255, null=False)
