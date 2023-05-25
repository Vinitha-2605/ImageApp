from django.db import models
from django.forms import ValidationError
import PIL.Image
import toml

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return self.category

def validate_image(image):
         config = toml.load('./config.toml')      
         img = PIL.Image.open(image)
         if img.size > config['img_size']:
            raise ValidationError(config['img_size_error'])
     
class Image(models.Model): 
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Images = models.ImageField(upload_to='photos', validators=[validate_image])
    Imagedata = models.BinaryField(null=True,blank=True)
    UserName = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.Title},{self.Description},{self.Category},{self.Images}"
    