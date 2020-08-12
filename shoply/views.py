from django.shortcuts import render

from .forms import LoginForm, RegisterForm


def home(request, *args, **kwargs):
    return render(request, "index.html", {})


def login(request, *args, **kwargs):

    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }
    return render(request, "login.html", context)


def register(request, *args, **kwargs):

    form = RegisterForm(request.POST or None)

    context = {
        "form": form
    }

    return render(request, 'register.html', context)
