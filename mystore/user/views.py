from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def signin(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home_page')
    else:
        form = UserRegForm()
    return render(request, 'signin.html', {'form': form})

def login_page(request):
    if  request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                messages.error(request, 'Ошибка входа. Проверьте вводимые данные.')
                return redirect('login_page')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})