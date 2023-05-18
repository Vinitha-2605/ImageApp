from django.db import models
from django.forms import ValidationError
import PIL.Image

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return self.category

def validate_image(image):
         img = PIL.Image.open(image)
         if img.size[0] > 1000:
            raise ValidationError("Image dimensions must not exceed 1000x1000 pixels.")
     
class Image(models.Model):
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Images = models.ImageField(upload_to='photos', validators=[validate_image])
    Imagedata = models.BinaryField(null=True,blank=True)
    UserName = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.Title},{self.Description},{self.Category},{self.Images}"
    