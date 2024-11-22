from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserForm


def signup(request):
    error_message = ""

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            error_message = "Invalid signup, please check your input and try again."

    else:
        form = UserForm()

    ctx = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", ctx)


def user_details(req, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(req, "user/user_details.html", {"user": user})
