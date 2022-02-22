from django.shortcuts import render
from .forms import RegisterForm


def registerUser(request):
    formObj = RegisterForm()
    return render(request, "users/register.html", {"form": formObj})
