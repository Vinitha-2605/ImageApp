from django.db import models
from Login.models import Register

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return self.category

class Image(models.Model):
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Images = models.ImageField(upload_to='photos', null=False)
    # UserName = models.ForeignKey(Register, on_delete=models.CASCADE)
    UserName = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.Title},{self.Description},{self.Category},{self.Images}"
    