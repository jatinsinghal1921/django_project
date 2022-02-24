from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def registerUser(request):
    if request.method == "POST":
        formObj = RegisterForm(request.POST)
        if formObj.is_valid():
            print("User Created : " + formObj.cleaned_data["username"])
            print("User email : " + formObj.cleaned_data["email"])
            print("User password : " + formObj.cleaned_data["password1"])
            formObj.save()
            return redirect("blog-home")
    else:
        formObj = RegisterForm()
    return render(request, "users/register.html", {"form": formObj})


@login_required(login_url='login')
def profile(request):
    return render(request, "users/profile.html")
