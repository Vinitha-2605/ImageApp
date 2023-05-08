from django.db import models

# Create your models here.

class Login(models.Model):
    Username = models.CharField(max_length=25)
    Password =  models.CharField(max_length=10)

    def __str__(self):
        return self.Username
    
class Register(models.Model):
    Username = models.CharField(max_length=10)
    Password = models.CharField(max_length=20)
    EMAIL = models.EmailField()
    def __str__(self):
        return f"{self.id},{self.Username}"