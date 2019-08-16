from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms

class RegisterValidation(forms.Form):
    login = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)

class LoginValidation(forms.Form):
    login = forms.CharField(max_length=30)
    password = forms.CharField(min_length=6)

# Create your views here.

def secret(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'index.html')

def logout_page(request):
    logout(request)
    return redirect('/login')

def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = LoginValidation(request.POST)
        if not form.is_valid():
            return HttpResponse('Заполните все поля!')

        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            return HttpResponse('Неверные данные!')
        else:
            login(request, user)
            return redirect('/')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        form = RegisterValidation(request.POST)
        if not form.is_valid():
            return HttpResponse('Заполните все поля!')

        user = User()
        user.username = request.POST.get('login')
        user.email = request.POST.get('email')
        user.set_password(request.POST.get('password'))
        user.save()

        login(request, user)

        return redirect('/')

