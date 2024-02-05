from app import models
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *



class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        



class HorairesSerializer(ModelSerializer):
    class Meta:
        model=  HoraireOuverture
        fields = '__all__'
        
class TarifSerializer(ModelSerializer):
    class Meta:
        model=  Tarif
        fields = '__all__'


class PartenaireSerializer(ModelSerializer):
    class Meta:
        model = Partenaire
        fields = '__all__'


class TouristeSerializer(ModelSerializer):
    class Meta:
        model = Touriste
        fields = '__all__'



class ItineraireSerializer(ModelSerializer):
    class Meta:
        model = Itineraire
        fields = '__all__'

class SiteSerializer(ModelSerializer):
    region = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all())  # Utilisez le champ PrimaryKeyRelatedField

    class Meta:
        model = SiteTouristique
        fields = '__all__'
