from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, "accounts/profile.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.role == "seller":
                return redirect("seller_dashboard")
            else:
                return redirect("customer_dashboard")
    else:
        messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.role == "seller":
                return redirect("seller_dashboard")
            else:
                return redirect("customer_dashboard")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserRegistrationForm()

    return render(request, "accounts/register.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def customer_dashboard(request):
    return redirect("product_list")


@login_required
def seller_dashboard(request):
    return render(request, "accounts/seller_dashboard.html")