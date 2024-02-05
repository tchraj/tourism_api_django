from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.views import View
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import viewsets



class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    
    

class SiteViewSet(viewsets.ModelViewSet):
    queryset = SiteTouristique.objects.all()
    serializer_class = SiteSerializer

class HoraireViewSet(viewsets.ModelViewSet):
    queryset = HoraireOuverture.objects.all()
    serializer_class = HorairesSerializer


class TarifViewSet(viewsets.ModelViewSet):
    queryset = Tarif.objects.all()
    serializer_class = TarifSerializer


class PartenaireViewSet(viewsets.ModelViewSet):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer



class TouristeViewSet(viewsets.ModelViewSet):
    queryset = Touriste.objects.all()
    serializer_class = TouristeSerializer



class ItineraireViewSet(viewsets.ModelViewSet):
    queryset = Itineraire.objects.all()
    serializer_class = ItineraireSerializer
    
    

# class SiteWithPartnersAndRegionList(generics.ListAPIView):
#     queryset = SiteTouristique.objects.all()
#     serializer_class = SiteSerializer

#     def get_queryset(self):
#         # Surcharge de la méthode get_queryset pour inclure les partenaires et la région associée à chaque site
#         queryset = SiteTouristique.objects.select_related('region').prefetch_related('partenaires').all()
#         return queryset