from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .forms import ObrazForm
from .models import Obraz
from django.conf import settings


@login_required(login_url="/users/", redirect_field_name=None)
def index(request):
    obrazy = Obraz.objects.all()
    
    return render(request, "index.html", {
        "obrazy_list": obrazy,
        "MEDIA_URL": settings.MEDIA_URL,
    })

@login_required(login_url="/users/", redirect_field_name=None)
def zobrazObraz(request, index):
    try:
        return render(request, "obraz.html", {
            "obraz": Obraz.objects.get(id=index),
        })
    except Obraz.DoesNotExist:
        return render(request, "404.html", {
            "chybova_hlaska": "Obraz nebyl nalezen",
        })
    except ValueError:
        return render(request, "404.html", {
            "chybova_hlaska": "Neplatný identifikátor",
        })
    except:
        return render(request, "404.html", {
            "chybova_hlaska": "Něco se pokazilo",
        })

@login_required(login_url="/users/", redirect_field_name=None)
def novyObraz(request):
    if request.method == "POST":
        form = ObrazForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/obrazy/')
        else:
            form = { "form": form }
            return render(request, "novy.html", form)
    else:
        form = { "form": ObrazForm() }
        return render(request, "novy.html", form)
    
@login_required(login_url="/users/", redirect_field_name=None)
def editObraz(request, index):
    if request.method == "POST":
        obraz = Obraz.objects.get(id=index)
        form = ObrazForm(request.POST, request.FILES, instance=obraz)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/obrazy/')
        else:
            form = { "form": form }
            return render(request, "edit.html", form)
    else:
        obraz = Obraz.objects.get(id=index)
        form = { "form": ObrazForm(instance=obraz), "obraz": obraz }
        return render(request, "edit.html", form)

@login_required(login_url="/users/", redirect_field_name=None)
def deleteObraz(request, index):
    obraz = Obraz.objects.get(id=index)
    obraz.delete()
    return HttpResponseRedirect('/obrazy/')

def error404(request, wrong):
    return render(request, "404.html", {
        "chybova_hlaska": "Stránka nebyla nalezena",
    })