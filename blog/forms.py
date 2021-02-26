from django.forms import ModelForm, TextInput, EmailInput,Textarea
from django.forms import ModelForm,Form
from django import forms
from .models import Formulaire
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormulaireForm(ModelForm):
    
    class Meta:
        model = Formulaire
        fields = ['nom','ville','quartier','niveauEnsei','matiere','commune','cv','experience','niveau','telephone','photopi','phOto','prix']
        widgets = {
            'nom': TextInput(attrs={'placeholder':'Quel est votre nom ?','class':'form-control'}),
            'ville': TextInput(attrs={'placeholder':'Ville actuelle ?','class':'form-control'} ),
            'commune': TextInput(attrs={'placeholder':'Commune (facultatif) ?','class':'form-control'}),
            'matiere': TextInput(attrs={'placeholder':'Domaine enseigné(EX:SCIENCE et/ou LITTERATURE) ?','class':'form-control'}),
            'quartier': TextInput(attrs={'placeholder':'Quartier ?','class':'form-control'}),
            'experience': TextInput(attrs={'placeholder':' experience ?','class':'form-control'}),
            'niveau': TextInput(attrs={ 'placeholder':'Quelle est votre niveau d\'etude ?','class':'form-control'}),
            'telephone': TextInput(attrs={'placeholder':'telephone ?','class':'form-control'}),
            'niveauEnsei': TextInput(attrs={'placeholder':'Quel niveau peux tu enseigner ?','class':'form-control'}),
        }
       

"""class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=['nom','email','objet','message']
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
"""
