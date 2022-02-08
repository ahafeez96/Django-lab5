from audioop import reverse
from cgitb import html
from multiprocessing import context
from re import M
from django.shortcuts import render,redirect , HttpResponsePermanentRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Myuser
from datetime import date
from .models import Intake , Track
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import Login_form
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

def home(request):
    html = """
    
   <!DOCTYPE html>
    <html lang="en">
     <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
     </head>
    <link
    rel="stylesheet"
    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
    crossorigin="anonymous"
     />
    <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Navbar</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only"></span></a>
            <a class="nav-link" href="about"
              >About <span class="sr-only"></span
            ></a>
            <a class="nav-link" href="contact"
              >Contact Us <span class="sr-only"></span
            ></a>
          </li>
                        </ul>
             </div>
            </nav>
            <h1>WELCOME</h1>
        </body>
        </html>
            """
    return HttpResponse(html)


def about(request):
    return render(request,'pages/about.html')


def landing (request):
  if (request.method=="GET"):
    return render(request,'pages/landing.html')
  else:
    logout(request)
    return render(request,'pages/landing.html')
def contact (request):
    return render(request,'pages/contact.html')


def login_view(request):
  if (request.method=="GET"):
    return render(request,'pages/login.html')
    print("if cond")
  else:
     user= Myuser.objects.filter(username=request.POST['username'],password=request.POST['password'])
     print("else cond",request)
     if(len(user)>0):
       context={}
       usname=request.POST['username']
       passwd=request.POST['password']
       user1= authenticate (username=usname, password=passwd)
       if user is not None:
        login(request,user1)
        return redirect(landing)
     else:
       context={}
       context['warning']='Invalid username or password'
       return render(request,'pages/login.html',context)
       


def register(request):
  if (request.method=='GET'):
    return render(request,'pages/register.html' )
  else:
   
      Myuser.objects.create(username=request.POST['username'],password=request.POST['password'])
      User.objects.create_user(username=request.POST['username'],password=request.POST['password'],is_staff=True)
      #return render (request, 'pages/login.html')
      return redirect (login_view)


def insert(request):
  context={}
  if(request.method=='GET'):
    return render(request,'pages/insert.html',{'lf':Login_form})
  else:
    print(request.POST)
    username=request.POST['username']
    password=request.POST['password']
   
    
    Myuser.objects.create(username=username,password=password)
    intakes=Myuser.objects.all()
    context['intakes']=intakes

    
   
    return render(request,'pages/list.html',context)


def updateintake(request,id):
    context={}
    Myuser.objects.filter(id=id).update()
    intakes = Myuser.objects.all()
    context['intakes'] = intakes
    return render(request, 'pages/list.html', context)


def deleteintake(request,id):
    context={}
    Myuser.objects.filter(id=id).delete()
    intakes = Myuser.objects.all()
    context['intakes'] = intakes
    return render(request, 'pages/list.html', context)


class TrackList(ListView):
  model=Track
class TrackCreate(SuccessMessageMixin,CreateView):
  model=Track
  fields=['name']
  success_url = reverse_lazy('landing')
  success_message = 'New Track Added Succefully'