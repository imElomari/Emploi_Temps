from django.db import models

# model Salles
class Salles(models.Model):
    # attributs
    nom = models.CharField(max_length=100)
    capacite = models.IntegerField()
    prise = models.BooleanField()
    # methode d'affichage
    def __str__(self):
        return self.nom