from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('success')
        else:
            return render(request, "accounts/login.html", {"error": "Invalid credentials."})
    return render(request, "accounts/login.html")

@login_required
def success_view(request):
    return render(request, "accounts/success.html", {"user": request.user})
