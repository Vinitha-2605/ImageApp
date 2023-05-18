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
         width, height = img.size
         if width > config['img_max_width'] or height > config['img_max_height']:
            raise ValidationError(f"Image dimensions must not exceed {config['img_max_width']}*{config['img_max_width'] } pixels.")
     
class Image(models.Model): 
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Images = models.ImageField(upload_to='photos', validators=[validate_image])
    Imagedata = models.BinaryField(null=True,blank=True)
    UserName = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.Title},{self.Description},{self.Category},{self.Images}"
    