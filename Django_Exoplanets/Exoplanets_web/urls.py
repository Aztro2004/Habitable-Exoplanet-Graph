from django.urls import path   #importa el modulo path de django
from . import views  #Importamos las vistas de las páginas de views.py

#Directorio de urls
urlpatterns = [
    path('',views.home,name='inicio'),   #vista principal de la página web
    path('Gallery/',views.galeria,name='galeria'), #vista galeria 
    path('All/',views.todos,name='todos') #vista de todos
    
]