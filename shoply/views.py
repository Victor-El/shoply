from django.shortcuts import render

from .forms import LoginForm, RegisterForm


def home(request, *args, **kwargs):
    return render(request, "index.html", {})



def privacy_policy(request, *args, **kwargs):
    return render(request, 'privacy_policy.html', {})


def terms_and_conditions(request, *args, **kwargs):
    return render(request, 'terms_and_conditions.html', {})


def login(request, *args, **kwargs):

    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }
    return render(request, "login.html", context)


def register(request, *args, **kwargs):

    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            return form.register()

    context = {
        "form": form
    }


    return render(request, 'register.html', context)
