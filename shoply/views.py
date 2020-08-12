from django.shortcuts import render

from .forms import LoginForm


def home(request, *args, **kwargs):
    return render(request, "index.html", {})


def login(request, *args, **kwargs):

    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }
    return render(request, "login.html", context)
