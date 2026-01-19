from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from datetime import date
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from memories.forms import LoginForm, RegisterForm, MemoryForm
from memories.models import Memory

def home(request):
    current_year=date.today().year
    context={
        "year":current_year,
    }
    return render(request, 'home.html', context)

@login_required(login_url='signIn')
def create_memory(request):
    current_year=date.today().year
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
        #   post.save()
          title=form.cleaned_data['title']
          post.slug=slugify(title)
          post.save()
          return redirect('read-memory')

        else:
            messages.error(request, "Post is not valid. Please try again...")
            return redirect('read-memory')
    else:
        form = MemoryForm()

    context={
        'year':current_year,
        'form':form,
    }

    return render(request, 'memory_form.html', context)
@login_required(login_url='signIn')
def read_memory(request):
    current_year=date.today().year
    memories=Memory.objects.select_related('author',).filter(author_id=request.user.id)
    context={
        'year':current_year,
        'memories':memories
    }
    return render(request,'memories_page.html',context)
@login_required(login_url='signIn')
def individual_memory(request, id):
    current_year=date.today().year
    post = get_object_or_404(Memory.objects.select_related('author'), id=id)
    context={
        'year':current_year, 
        'memory':post,
    }
    return render(request, 'memory.html', context)

@login_required(login_url='signIn')
def update_memory(request, id):
    current_year=date.today().year
    memory=get_object_or_404(Memory, id=id)
    # memory = get_object_or_404(Memory.objects.select_related('author'), id=id)
    
    if request.method=='POST':
        form=MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            updated_form=form.save(commit=False)
            updated_form.author=request.user
            title=form.cleaned_data['title']
            updated_form.slug=slugify(title)
            updated_form.save()
            messages.success(request, "Post updated Successfully!")
            return redirect('read-memory')
        else:
            messages.error(request, 'Updated Failed. Please try again...')
            return redirect('read-memory')
    else:
        form=MemoryForm(instance=memory)
    context={
        "year":current_year, 
        "form":form,
        "memory":memory
    }
    return render(request, 'memory_form.html', context)

@login_required(login_url='signIn')
def delete_memory(request, id):
    current_year=date.today().year
    post = get_object_or_404(Memory.objects.select_related('author'), id=id)
    post.delete()
    messages.success(request, 'Post deleted successfully .')
    return redirect('read-memory')
