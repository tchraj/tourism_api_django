from django.db import models

# Create your models here.
class RegionEnum(): 
    choices = [
        ("MARITIME", "Maritime"),
        ("PLATEAUX", "Plateaux"),
        ("CENTRALE", "Centrale"),
        ("KARA", "Kara"),
        ("SAVANES", "Savanes"),

    ]
        
class TypePartenaire(): 
    choices = [
    ("HOTEL", "HOTEL"),
    ("RESTAURANT", "RESTAURANT"),
    
    ]
       
       
class Region(models.Model):
    nom_region = models.CharField(max_length=30,choices=RegionEnum.choices)
    nombre_sites = models.PositiveIntegerField()

    def __str__(self):
        return self.nom_region
    
class Partenaire(models.Model):
    nom_partenaire = models.CharField(max_length=60)
    localisation = models.CharField(max_length=120)
    services = models.TextField
    # sites = models.ManyToManyField(SiteTouristique,blank=True,related_name='partenaires')
    type_partenaire = models.CharField(max_length=60, choices=TypePartenaire.choices,blank=True)

    def __str__(self):
        return self.nom_partenaire
       
       
class SiteTouristique(models.Model):
    nom_site = models.CharField(max_length=100)
    # nombre_partenaires = models.PositiveIntegerField()
    localisation = models.CharField(max_length=120)
    services = models.TextField()
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    partenaires = models.ManyToManyField(Partenaire, blank=True, related_name="sites")
    
    def __str__(self):
        return self.nom_site


    

        
class Touriste(models.Model):
    nom_touriste = models.CharField(max_length=60)
    prenoms_touriste = models.CharField(max_length=60)
    email = models.EmailField
    tel = models.CharField(max_length=15)
    sites= models.ManyToManyField(SiteTouristique)
    partenaires = models.ManyToManyField(Partenaire, null=True, blank=True)

    
    def nom_complet(self):
        nom_complet = f"{self.nom_touriste} {self.prenoms_touriste}"
        return nom_complet
    
    def __str__(self):
        return self.nom_touriste
    
class Itineraire(models.Model):
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.ForeignKey(SiteTouristique, on_delete=models.CASCADE)  # Ajout de on_delete
    destination = models.ForeignKey(Partenaire, on_delete=models.CASCADE)  # Ajout de on_delete

    def __str__(self):
        return str(self.destination)
    
class HoraireOuverture(models.Model):
    site_touristique = models.ForeignKey(SiteTouristique, on_delete=models.CASCADE)
    jour = models.CharField(max_length=10, choices=[
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
        ('samedi', 'Samedi'),
        ('dimanche', 'Dimanche'),
    ])
    heure_ouverture = models.TimeField()
    heure_fermeture = models.TimeField()

    def __str__(self):
        return f"{self.site_touristique.nom_site} - {self.jour} de {self.heure_ouverture} à {self.heure_fermeture}"
    
    
    
class Tarif(models.Model):
    site_touristique = models.ForeignKey(SiteTouristique, on_delete=models.CASCADE)
    categorie = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.site_touristique.nom_site} - {self.categorie}: {self.prix} FCFA"