from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
import base64
import logging

from .forms import ImageForm, CategoryForm
from .models import Image, Category

# Create your views here.
logging.basicConfig(level=logging.INFO)

def upload(request):
    if (request.method == "POST"):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
          img =  request.FILES['Images']
          with img.open() as image_file:
           encoded_string = image_file.read()
          imagedetail = Image(Title= form.cleaned_data['Title'],
                               Description = form.cleaned_data['Description'],
                               Category = form.cleaned_data['Category'],
                               Imagedata= encoded_string, 
                               UserName = request.session['User'])
          imagedetail.save()
          return HttpResponse("Submitted Successfully")
        else:           
            return render(request,  "image.html",{
            "forms": form
         })
    else:  
     form = ImageForm()
     return render(request, "image.html",{
        "forms": form
    })

def addcategory(request):
    if (request.method == "POST"):
        form = CategoryForm(request.POST) 
        
        if form.is_valid():
           form.save()
           return HttpResponse("Submitted Successfully")
    else:   
     form = CategoryForm()
     return render(request, "Category.html",{
        "forms": form
    })

def imagedetail(request, id):
   image = Image.objects.get(id=id)
   return render(request, "image-detail.html",{
      "images": image
   })

def searchimage(request):
   Title = request.GET
   Description = request.GET
   image = Image.objects.filter(Q(Title=Title['Title']) | 
                                Q(Description=Description['Description']))                       
   return render(request, "searchimages.html",{
      "images": image   
   })

def imageview(request):
   form = Category.objects.values()
   image = Image.objects.all().values()
   data = list()
   for imagedata in image:
      if imagedata['Imagedata'] is not None:
       imagedata['Imagedata'] = base64.b64encode(imagedata['Imagedata']).decode('utf-8')
      data.append(imagedata)
      logging.info(data)

      return render(request, "searchimages.html",{
       "images": data,
        "categorys": form
    })

def searchcategory(request):
    if (request.method == "POST"):
       category = request.POST['Images']

       image = Image.objects.filter(Category=category)
       return render(request, "searchimages.html",{
          "images": image 
       })
    else:
       form = Category.objects.values()
       return render(request, "searchimages.html",{
        "categorys": form
    })