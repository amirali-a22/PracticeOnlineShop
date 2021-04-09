from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import LoginUserForm, RegisterUserForm
from accounts.models import User


def login_user(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are logged in. You can not Login!!!', 'warning')
        return redirect('shop:home')
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in', 'success')
                return redirect('shop:home')
            else:
                messages.warning(request, 'your password or email is wrong!', 'danger')
    form = LoginUserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login_user.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'you logged out', 'danger')
    return redirect('shop:home')


def register_user(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are logged in. You can not register!!!', 'warning')
        return redirect('shop:home')
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(email=form.cleaned_data['email'], full_name=form.cleaned_data['fullname'],
                                            password=form.cleaned_data['password'])
            login(request, user)
            messages.success(request, 'you registered successfully', 'success')
            return redirect('shop:home')
        else:
            messages.error(request, 'try again', 'danger')
    form = RegisterUserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/register_user.html', context)
