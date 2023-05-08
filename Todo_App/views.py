from django.shortcuts import render, redirect
from . forms import register, tasks
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Task

# Create your views here.


def home(request):
    form = Task.objects.all()
    return render(request, 'home.html',{'form':form})

def logins(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "invalid credentials")

    return render(request, 'login.html')


def reg(request):
    form = register()
    if request.method == "POST":
        form = register(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created for '+user)
            return redirect('/')
        else:
            messages.error(request, form.errors.get('username'))
    context = {'form': form}
    return render(request, 'register.html', context)


def logouts(request):
    logout(request)
    return redirect('home')


def task(request):
    return render(request, 'task.html')


def add_task(request):
    if request.method == "POST":
        form = tasks(request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            return redirect('/')
    form = tasks()
    context={'form':form}
    return render(request, 'add_task.html', context)


def task_edit(request, request_ID):
    forms = Task.objects.get(pk=request_ID)
    data = tasks(request.POST or None, instance=forms)
    if data.is_valid():
        update=data.save(commit=False)
        update.user = request.user
        update.save()
        return redirect('/')
    context={'form':forms, 'data':data}
    return render(request, 'task_edit.html', context)

def delete_task(request, request_ID):
    forms = Task.objects.get(pk=request_ID)
    forms.delete()
    return redirect('/')

