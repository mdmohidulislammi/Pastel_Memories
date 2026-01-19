from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from datetime import date
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from memories.forms import LoginForm, RegisterForm,Update_User_Form
from memories.models import Memory

# Create your views here.
@login_required(login_url='signIn')
def dashboard(request, id):
    current_year=date.today().year 
    context={
        'year':current_year,
    }
    return render(request, 'dashboard.html', context)
# @login_required(login_url='signIn')
def manager_dashboard(request):
    current_year=date.today().year
    id=request.user.id 
    if not request.user.is_authenticated:
        return redirect('signIn')    
    users=User.objects.all()
    context={
        'year':current_year,
        'users':users,
    }
    return render(request, 'manager_dashboard.html', context)
def signIn(request):
    current_year = date.today().year
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form=LoginForm()
    
    context={
        'year':current_year,
        'form':form
    }
    return render(request, 'login.html', context)
def logOut(request):
    logout(request)
    return redirect('home')

def signUp(request):
    current_year = date.today().year
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard', id=request.user.id)
            else:
                return redirect('home')
        
    else:
        form = RegisterForm()

    context = {
        'form': form,
        'year': current_year
    }
    return render(request, 'register.html', context)


@login_required(login_url='signIn')
def update(request, id):
    current_year = date.today().year
    user=get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = Update_User_Form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            if request.user.is_superuser:
                return redirect('manager' )
            else:
                return redirect('dashboard', id=user.id) 
    else:
        form = Update_User_Form(instance=user)

    context = {
        'form': form,
        'year': current_year
    }
    return render(request, 'register.html', context)


@login_required
def delete_user(request,id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        user.delete()
        if user.is_superuser:
             return redirect('dashboard')
        else:
            return redirect('home')  
    else:
        user.delete()
        if request.user.is_superuser:
             return redirect('manager')
        else:
            return redirect('home') 
    
