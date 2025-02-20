from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usernames = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created for {usernames}! You can now login"
            )
            return redirect("accounts:login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})
@login_required
def profile(request):
    return render(request, "accounts/profile.html")