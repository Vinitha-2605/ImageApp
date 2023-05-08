from django.shortcuts import render
from .forms import ImageForm, CategoryForm
from .models import Image, Category
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

# Create your views here.

def upload(request):
    if (request.method == "POST"):
        form = ImageForm(request.POST, request.FILES)

        # searchimage(request)
        
        if form.is_valid():
           print( request.session['User'])
           imagedetail = Image(Title= form.cleaned_data['Title'],
                               Description = form.cleaned_data['Description'],
                               Category = form.cleaned_data['Category'],
                               Images = form.cleaned_data['Images'],
                               UserName = request.session['User'])
           imagedetail.save()
           return HttpResponse("Submitted Successfully")
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
     image = Image.objects.all()
     return render(request, "searchimages.html",{
        "images": image,
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