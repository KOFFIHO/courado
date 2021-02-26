from django.contrib import admin
from .models import Repetiteur
from .models import Formulaire 
from .models import Note
from .models import Defile
from .models import Offre
# Register your models here.

class AdminRepetiteur(admin.ModelAdmin):
    list_display = ['nom', 'ville', 'quartier']


class AdminFormulaire(admin.ModelAdmin): 
    list_display = ['nom', 'ville', 'quartier']


admin.site.register(Repetiteur, AdminRepetiteur)

admin.site.register(Formulaire, AdminFormulaire)

admin.site.register(Note) 

admin.site.register(Defile)
 
admin.site.register(Offre) 


