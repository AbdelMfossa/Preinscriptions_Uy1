from django.urls import path
from falshfsfse.views import *

app_name = 'falshfsfse'

urlpatterns = [
    path('', civilite, name='civilite'), 
    path('filiation/', filiation, name='filiation'), 
    #path('faculte/', faculte, name='faculte'),
    #path('diplome/', diplome, name='diplome'),
    #path('sport/', sport, name='sport'),
    #path('autres/', autres, name='autres'),
    
]