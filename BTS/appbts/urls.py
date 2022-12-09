from django.urls import path #importo los paths para que queden dentro de la app
from .views import * #importo las views


urlpatterns = [
    path("inicio", inicio, name="inicio"),

]