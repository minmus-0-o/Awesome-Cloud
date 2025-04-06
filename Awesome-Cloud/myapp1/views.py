from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import MyFiles
# from django.db.models.signals import post_delete
# from django.dispatch import receiver
# import os
# from django.core.files.storage import default_storage

# Ура, я сэкономил несколько милисекунд, удалив ненужные импорты! ^-^

def enter(request):
    return render(request, 'index.html')

def sign(request):
    if request.POST:
        print("Логин:", request.POST['login'])
        print("Пароль:", request.POST['password'])
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, 'login.html')

def registration(request):
    if request.POST:
        print(request.POST)
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if not User.objects.filter(username=request.POST["login"]):
                User.objects.create_user(username=request.POST['login'], password=request.POST['password1'])
                return redirect("login")
    return render(request, 'registration.html')

def page(request):
    if request.user.is_authenticated:
        all_files = MyFiles.objects.filter(owner=request.user)
        print(request.user)
        context = {
            'all_files': all_files
        }

        if request.POST:
            MyFiles.objects.create(
            text = request.POST.get('text'),
            file = request.FILES.get('file'), 
            owner = request.user
            )

        return render(request, 'index.html', context)
    else:
        return redirect('login')
    
def delete(request, file_id):
    if request.method == 'POST':
        MyFiles.objects.get(id=file_id).delete()
        return redirect('home')