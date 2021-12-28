from django.db import models
from django.db.models.fields.related import ForeignKey

from GestionClient.models import Client
import datetime


class Commande(models.Model):
    DateCommande = models.CharField(blank=False,max_length=20)
    prix = models.FloatField(blank=False)
    client = ForeignKey(Client,on_delete=models.CASCADE)

        