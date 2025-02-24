from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Obraz, Technika
from .forms import ObrazForm
from autori.models import Autor
from django.contrib.auth.decorators import login_required

# Create your views here.

def cena_rozdel(cena):
    cena_puv = str(cena)
    cena_puv_len = len(cena_puv)
    cena = cena_puv[:3] if cena_puv_len % 3 == 0 else cena_puv[:cena_puv_len % 3]
    cena_puv = cena_puv[3:] if cena_puv_len % 3 == 0 else cena_puv[cena_puv_len % 3:]

    while len(cena_puv) >= 3:
        cena = cena + " " + cena_puv[-3:]
        cena_puv = cena_puv[:-3]

    return cena

@login_required(login_url='/uzivatele/login/')
def obraz_list(request):
    obrazy = Obraz.objects.all()
    autori = Autor.objects.all()
    techniky = Technika.objects.all()

    autor_id = request.GET.get('autor', None)
    itechnika_id = request.GET.get('technika', None)

    if autor_id:
        obrazy = obrazy.filter(autor=autor_id)
    if itechnika_id:
        obrazy = obrazy.filter(technika__id=itechnika_id)

    for obraz in obrazy:
        obraz.cena = cena_rozdel(obraz.cena)

    return render(request, 'seznam_obrazu.html', {
        "obrazy_list": obrazy,
        "autori_list": autori,
        "techniky_list": techniky
    })

@login_required(login_url='/uzivatele/login/')
def obraz_detail(request, id):
    try:
        obraz = Obraz.objects.get(id=id)
        obraz.cena = cena_rozdel(obraz.cena)

        return render(request, 'detail_obrazu.html', {'obraz': obraz})
    except:
        return render(request, '404.html', {
            "chybova_hlaska": "Obraz nebyl nalezen."
        })

@login_required(login_url='/uzivatele/login/')
def obraz_create(request):
    if request.method == 'POST':
        form = ObrazForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/obrazy/')
    else:
        form = ObrazForm()

    return render(request, 'novy_obraz.html', {
        'form': form,
        'stranka': "novy"
    })

@login_required(login_url='/uzivatele/login/')
def obraz_edit(request, id):
    obraz = Obraz.objects.get(id=id)

    if request.method == "POST":
        form = ObrazForm(request.POST, request.FILES, instance=obraz)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/obrazy/')
    else:
        form = ObrazForm(instance=obraz)

    return render(request, 'novy_obraz.html', {
        'form': form,
        'stranka': "edit",
        'obraz': obraz
    })

@login_required(login_url='/uzivatele/login/')
def obraz_delete(request, id):
    obraz = Obraz.objects.get(id=id)
    obraz.img.delete()
    obraz.delete()
    return HttpResponseRedirect('/obrazy/')