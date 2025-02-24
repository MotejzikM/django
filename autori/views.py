from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Autor
from .forms import AutorForm
from obrazy.models import Obraz
from django.contrib.auth.decorators import login_required
from obrazy.views import cena_rozdel
from uzivatele.templatetags import custom_filters

# Create your views here.

@login_required(login_url='/uzivatele/login/')
def autor_list(request):
    return render(request, 'seznam_autoru.html', {
        "autori_list": Autor.objects.all()
    })

@login_required(login_url='/uzivatele/login/')
def autor_detail(request, id):
    try:
        autor = Autor.objects.get(id=id)
        autor.obrazy = Obraz.objects.filter(autor=autor)

        for obraz in autor.obrazy:
            obraz.cena = cena_rozdel(obraz.cena)

        return render(request, 'detail_autora.html', {'autor': autor})
    except:
        return render(request, '404.html', {
            "chybova_hlaska": "Autor nebyl nalezen."
        })

@login_required(login_url='/uzivatele/login/')
def autor_create(request):
    if custom_filters.has_group(request.user, 'Editoři'):
        if request.method == 'POST':
            form = AutorForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/autori/')
        else:
            form = AutorForm()

        return render(request, 'novy_autor.html', {
            'form': form,
            'stranka': "novy"
        })
    

@login_required(login_url='/uzivatele/login/')
def autor_edit(request, id):
    if custom_filters.has_group(request.user, 'Editoři'):
        autor = Autor.objects.get(id=id)

        if request.method == 'POST':
            form = AutorForm(request.POST, request.FILES, instance=autor)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/autori/')
        else:
            autor.narozen = str(autor.narozen)
            autor.umrti = str(autor.umrti)

            form = AutorForm(instance=autor)

        return render(request, 'novy_autor.html', {
            'form': form,
            'stranka': "edit",
            'autor': autor
        })


@login_required(login_url='/uzivatele/login/')
def autor_delete(request, id):
    autor = Autor.objects.get(id=id)
    autor.obrazy.all().delete()
    autor.img.delete()
    autor.delete()
    return HttpResponseRedirect('/autori/')