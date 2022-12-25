from django.urls import path #importo los paths para que queden dentro de la app
from .views import * #importo las views


urlpatterns = [
    path("inicio", inicio, name="inicio"),
    path("bts", bts, name="bts"),
    path("coreasur", coreasur, name="coreasur"),
    path("army", army, name="army"),

]