from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def reg(request):
        if request.method == 'POST':
            errors = User.objects.validate(request.POST)
            if len(errors) > 0:
                for key, values in errors.items():
                    messages.error(request, values)
                return redirect("/")
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            print(pw_hash)
            new_user = User.objects.create(fname=request.POST['fname'], lname=request.POST['lname'], email=request.POST['email'], password=pw_hash)
            request.session['name'] = new_user.fname
            request.session['user_id'] = new_user.id
            request.session['function'] = "Registered"
            print(new_user.fname)
        return redirect('/')

def login(request):
    if request.method == 'POST':
        current_user = User.objects.filter(email=request.POST['email'])
        if len(current_user) > 0:
            current_user = current_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), current_user.password.encode()):
                request.session['name'] = current_user.fname
                request.session['user_id'] = current_user.id
                request.session['function'] = "Logged In"
            return redirect('/search')
    return redirect('/') 

def search(request):
    return render(request,'search.html')