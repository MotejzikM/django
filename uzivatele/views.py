from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    return HttpResponseRedirect('/uzivatele/login/')

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect('/autori/')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {
        'form': form
    })

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/uzivatele/login/')