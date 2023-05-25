import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from .models import Register
from django.contrib.auth import login, authenticate

# Create your views here.

def loginpage(request):
    if (request.method == "POST"):
       form = LoginForm(request.POST)

       if form.is_valid():
        user = Register.objects.get(Username = form.cleaned_data['Username'],
                                    Password =form.cleaned_data["Password"])
        
        if user is not None:
         request.session['User'] = user.Username
         print(request.session.get('User'))
         return HttpResponseRedirect("/image")
        else:
           return HttpResponse("Username or Password is incorrect")
    else:  
     form = LoginForm()
    return render(request, 'LoginForm.html',{
        "loginDetails": form
    })

def signup(request):
    if (request.method == "POST"):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save();
            return HttpResponse("Submitted Successfully");
    else:
     form = RegisterForm()
    return render(request, 'Register.html', {
        "RegisterDetails": form
    })

def logout():
   return HttpResponseRedirect("/Login")