from django.db import models
from django.db.models import fields
from django.forms import ModelForm

class Client(models.Model):
    
    nom = models.CharField(blank=False,max_length=30)
    prenom = models.CharField(blank=False,max_length=30)
    poste  = models.CharField(blank=True,max_length=50)
    email = models.EmailField(blank=False,max_length=30)
    adresse = models.CharField(blank=False,max_length=50)


class ClientModel(ModelForm):
    class Meta: 
        model = Client
        fields = ('nom','prenom','poste','email','adresse')
        


        