from django.shortcuts import render
from .forms import *

# Create your views here.
def accueil(request):
    return render(request, 'falshfsfse/home.html')

def civilite(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    #context = {'civilite_form': CivilForm(), 'filiation_form': FiliationForm()}
    context = {'civilite_form': CivilForm()}
    return render(request, 'falshfsfse/civilite.html', context)

def filiation(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    context = {'filiation_form': FiliationForm()}
    return render(request, 'falshfsfse/filiation.html', context)

def faculte(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = FiliationForm()

    return render(request, 'falshfsfse/faculte.html', {'form': form})

def diplome(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = FiliationForm()

    return render(request, 'falshfsfse/diplome.html', {'form': form})

def sport(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = FiliationForm()

    return render(request, 'falshfsfse/sport.html', {'form': form})

def autres(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = FiliationForm()

    return render(request, 'falshfsfse/autres.html', {'form': form})