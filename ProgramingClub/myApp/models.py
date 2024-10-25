from django.db import models

# Create your models here.
class myApp(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

def ____str_____(self):
         return  f"{self.firstname} {self.lastname}"