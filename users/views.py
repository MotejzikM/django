from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            render(request, "error.html")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")