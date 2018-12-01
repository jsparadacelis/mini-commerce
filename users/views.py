from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Client
from .forms import LoginForm, SignUpForm


def login_view(request):

    if request.method == "POST":

        form = LoginForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            user = authenticate(
                request, 
                username = data["username"], 
                password = data["password"]
            )

            if user and user.is_staff:
                login(request, user)
                return redirect("list_trans")
            elif user :
                login(request, user)
                return redirect("list_products")
            else:
                messages.error(request,'usuario o contraseña incorrecta')
                return redirect('login_view')
        else:
            pass
            
    else:
        form = LoginForm()


    return render(
        request,
        'users/login.html',
        {
            'form': form
        }
    )


@login_required
def log_out(request):
    logout(request)
    return redirect("login_view")


def sign_up(request):

    form_signup = SignUpForm()
    if request.method == 'POST':

        form_signup = SignUpForm(request.POST)
        if form_signup.is_valid():
            form_signup.save()
            return redirect("login_view")


    return render(
            request, 
            'users/login.html',
            {
                "form_signup" : form_signup
            }
    )    