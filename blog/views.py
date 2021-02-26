from django.shortcuts import render,redirect, get_object_or_404
from .models import Repetiteur 
from .models import Formulaire
from .models import Ville
from .forms import  FormulaireForm
from .models import Note 
from .models import Defile
from .models import Offre
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
# Create your views here.

def index(request):
    defiles = Defile.objects.all();
    notes = Note.objects.all(); 
    offres = Offre.objects.all();
    context={
        'defiles' :defiles,
        'notes' :notes,
        'offres' :offres,
        }
    return render(request, 'index.html' , context)

def inscription(request):
    defiles = Defile.objects.all();
    notes = Note.objects.all();
    form = FormulaireForm()
    offres = Offre.objects.all();
    context={'form':form,
    'offres' :offres,
    'defiles' :defiles,
    }
    message= ""
    error=""
    if request.method == 'POST':
        form = FormulaireForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            message="Inscription validée ."
            return redirect('inscription')
        else:
            print(form.errors) 
            error="ok"
            form = FormulaireForm() 
    
    context={
        'defiles' :defiles,
        'form':form,
        'message':message,
        'error':error,
        'notes' :notes,
        'offres' :offres,
        }
    return render(request, 'inscription.html' , context)

def resultats(request): 
    #repetiteurs = None
    #formulaires =Formulaire.objects.filter(available=True).order_by('-created_at')[:12]
    defiles = Defile.objects.all();
    formulaires = None
    villes = Ville.get_all_villes()
    villeID = request.GET.get('ville')
    if villeID:
        formulaires = Formulaire.objects.filter(ville=villeID)
        #repetiteurs = Repetiteur.objects.filter(ville=villeID)
        #notes = Note.objects.filter(ville=villeID);
    else:
        #repetiteurs = Repetiteur.objects.all();
        formulaires = Formulaire.objects.all();
        notes = Note.objects.all();
        offres = Offre.objects.all();
        
    data = {}
    data['defiles'] = defiles
    data['offres'] = offres
    data['notes'] = notes
    data['formulaires'] = formulaires
    #data['repetiteurs'] = repetiteurs
    data['villes'] = villes
    #paginator = Paginator(formulaires, 1)
    #page = request.GET.get('page')
    #formulaires = paginator.page(page)
    #try:
     #   formulaires = paginator.page(page)
    #except PageNotAnInteger:
     #   formulaires = paginator.page(1)
    
    #except EmptyPage:
     #   formulaires = paginator.page(paginator.num_pages)


    return render(request, 'resultats.html', data)


def rechercheform(request):
    #nombre=0
    message = ""
    query = request.GET.get('query')
    if not query:
        formulaires = Formulaire.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        formulaires = Formulaire.objects.filter(ville__icontains=query)
        if not formulaires.exists():
            formulaires = Formulaire.objects.filter(nom__icontains=query)
        if not formulaires.exists():
            formulaires = Formulaire.objects.filter(niveau__icontains=query)
        if not formulaires.exists():
            formulaires = Formulaire.objects.filter(commune__icontains=query)
        if not formulaires.exists():
            formulaires = Formulaire.objects.filter(quartier__icontains=query)
        if not formulaires.exists():
            formulaires = Formulaire.objects.filter(matiere__icontains=query) 
        if not formulaires.exists() :
            message ="Aucun resulat trouvé pour %s"%query
            context = {
                'message':message,
                }

    context = {
        'formulaires':formulaires,
        #'repetiteurs':repetiteurs,
        'message':message,
    }
    return render(request, 'resultats.html', context)

def details(request ,details_id):
    id = int(details_id)
    #repetiteur = Repetiteur.objects.get(id=details_id)
    #formulaire = get_object_or_404(Formulaire, id=details_id)
    formulaire = Formulaire.objects.get(id=details_id)
    notes = Note.objects.all();  
    offres = Offre.objects.all();  
    defiles = Defile.objects.all();
    context={
        'defiles' :defiles,
        'formulaire': formulaire,
        #'repetiteur': repetiteur,
        'notes' :notes,
        'offres' :offres,
        }
    return render(request, 'details.html' , context)  
