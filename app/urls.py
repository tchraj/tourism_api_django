from django.shortcuts import render
from django.urls import include,path
from app.serializers import *
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings
from django.urls import path

    





router = DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'sites', SiteViewSet)
router.register(r'partenaires', PartenaireViewSet)
router.register(r'touristes', TouristeViewSet)
router.register(r'itineraires', ItineraireViewSet)
router.register(r'horaires',HoraireViewSet)
router.register(r'tarifs',TarifViewSet)


urlpatterns = [
    path('',include(router.urls)),
    # path('details_sites/', SiteWithPartnersAndRegionList.as_view(), name='site-list'),
   
]
