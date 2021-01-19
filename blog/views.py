from django.shortcuts import render,redirect
from .models import Repetiteur 
from .models import Formulaire
from .models import Ville
from .forms import  FormulaireForm
from .models import Note
from django.views import View
# Create your views here.

def index(request):
    notes = Note.objects.all();
    form = FormulaireForm()
    context={'form':form}
    message= ""
    error=""
    if request.method == 'POST':
        form = FormulaireForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            message="Inscription validée ."
            return redirect('index')
        else:
            print(form.errors) 
            error="ok"
            form = FormulaireForm() 
    
    context={
        'form':form,
        'message':message,
        'error':error,
        'notes' :notes,
        }
    return render(request, 'index.html' , context)

def resultats(request):
    repetiteurs = None
    villes = Ville.get_all_villes()
    villeID = request.GET.get('ville')
    if villeID:
        repetiteurs = Repetiteur.objects.filter(ville=villeID)
        #notes = Note.objects.filter(ville=villeID);
    else:
        repetiteurs = Repetiteur.objects.all();
        notes = Note.objects.all();
    data = {}
    data['notes'] = notes
    data['repetiteurs'] = repetiteurs
    data['villes'] = villes
    return render(request, 'resultats.html', data)


def rechercheform(request):
    #nombre=0
    message = ""
    query = request.GET.get('query')
    if not query:
        repetiteurs = Repetiteur.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        repetiteurs = Repetiteur.objects.filter(ville__icontains=query)
        if not repetiteurs.exists():
            repetiteurs = Repetiteur.objects.filter(nom__icontains=query)
        if not repetiteurs.exists():
            repetiteurs = Repetiteur.objects.filter(niveau__icontains=query)
        if not repetiteurs.exists():
            repetiteurs = Repetiteur.objects.filter(commune__icontains=query)
        if not repetiteurs.exists():
            repetiteurs = Repetiteur.objects.filter(quartier__icontains=query) 
        if not repetiteurs.exists() :
            message ="Aucun resulat trouvé pour %s"%query
            context = {
                'message':message,
                }

    context = {
        'repetiteurs':repetiteurs,
        'message':message,
    }
    return render(request, 'resultats.html', context)

def details(request ,details_id):
    id = int(details_id)
    repetiteur = Repetiteur.objects.get(id=details_id)
    notes = Note.objects.all();
    
    context={
        'repetiteur': repetiteur,
        'notes' :notes
        }
    return render(request, 'details.html' , context)  
