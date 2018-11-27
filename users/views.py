from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Client


def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

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
        return render(request, 'users/login.html')


@login_required
def log_out(request):
    logout(request)
    return redirect("login_view")


def sign_up(request):

    if request.method == 'POST':

        data = request.POST
        user = User.objects.create_user(
            data["username"],
            data["mail"],
            data["password"]
        )
        user.save()


        client = Client.objects.create(user = user, terminal = data["terminal_id"])
        client.save()

        user_created = authenticate(request, username=data["username"], password=data["password"])
        if user_created :
            login(request, user_created)
            return redirect("list_products")

    else:
        return render(request, 'users/login.html', {"sign_up":"true"})