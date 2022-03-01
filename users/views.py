from turtle import home
from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdationForm, ProfileUpdationform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def registerUser(request):
    if request.method == "POST":
        formObj = RegisterForm(request.POST)
        if formObj.is_valid():
            print("User Created : " + formObj.cleaned_data["username"])
            print("User email : " + formObj.cleaned_data["email"])
            print("User password : " + formObj.cleaned_data["password1"])
            formObj.save()
            new_user = authenticate(
                username=formObj.cleaned_data['username'], password=formObj.cleaned_data['password1'])
            login(request, new_user)
            return redirect("blog-home")
    else:
        formObj = RegisterForm()
    return render(request, "users/register.html", {"form": formObj})


@login_required(login_url='login')
def profile(request):
    if request.method == "POST":
        u_form = UserUpdationForm(request.POST, instance=request.user)
        p_form = ProfileUpdationform(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("profile")
    else:
        u_form = UserUpdationForm(instance=request.user)
        p_form = ProfileUpdationform(instance=request.user.profile)
    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, "users/profile.html", context)
