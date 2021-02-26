from django.db import models

# Create your models here.

class Ville(models.Model):
    nom = models.CharField(max_length=100)

    @staticmethod
    def get_all_villes():
        return Ville.objects.all()

    def __str__(self):
        return self.nom


class Repetiteur(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    prix = models.IntegerField(blank=True , null=True)
    commune = models.CharField(max_length=100, blank=True, null=True)
    quartier = models.CharField(max_length=100)
    matiere = models.CharField( max_length=500)
    cv = models.FileField(upload_to='stokRepetiteur',blank=True , null=True)
    experience = models.IntegerField()
    niveau = models.CharField(max_length=200)
    niveauEnsei = models.CharField(max_length=1000)
    telephone = models.IntegerField()
    photopi = models.FileField(upload_to='stokRepetiteur')
    phOto = models.ImageField(upload_to='stokRepetiteur')

    def __str__(self):
        return self.nom
    
    
    @staticmethod
    def get_all_repetiteurs():
        return Repetiteur.objects.all()

    @staticmethod
    def get_all_repetiteurs_by_repetiteursid(ville_id):
        if ville_id:
            return Repetiteur.objects.filter(ville = ville_id)
        
        else:
            return Repetiteur.get_all_repetiteurs()


class Formulaire(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    prix = models.IntegerField(blank=True , null=True, default=0)
    quartier = models.CharField(max_length=100)
    matiere = models.CharField( max_length=500)
    commune = models.CharField(max_length=100, blank=True, null=True)
    cv = models.FileField(upload_to='photoform',blank=True)
    experience = models.CharField(max_length=50)
    niveau = models.CharField(max_length=200)
    niveauEnsei = models.CharField(max_length=1000)
    telephone = models.CharField(max_length=50)
    photopi = models.FileField(upload_to='photoform',blank=True)
    phOto = models.ImageField(upload_to='photoform',blank=True)

    def register(self):
        self.save()
    
    def __str__(self):
        return self.nom
    
    @staticmethod
    def get_all_formulaires():
        return Formulaire.objects.all()

    @staticmethod
    def get_all_formulaires_by_formulairesid(ville_id):
        if ville_id:
            return Formulaire.objects.filter(ville = ville_id)
        
        else:
            return Formulaire.get_all_formulaires()



class Note(models.Model):
    photo = models.ImageField(upload_to='note')
    nom = models.CharField(max_length=100)
    matiere = models.CharField( max_length=500)

    def __str__(self):
        return self.nom

class Defile(models.Model):
    image1= models.ImageField(upload_to='stock')
    description = models.TextField()
    image2= models.ImageField(upload_to='stock')
    description1 = models.TextField()
    image3= models.ImageField(upload_to='stock')
    description2 = models.TextField()
    telephone = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description

class Offre(models.Model):
    contenu = models.TextField()

    def __str__(self):
        return self.contenu
