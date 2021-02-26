from django.urls import path, include
from django.conf.urls import url
from .views import index, resultats, rechercheform , details, inscription
from courAD import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index, name="index" ),
    path('resultats',resultats, name="resultats" ),
    path('inscription',inscription, name="inscription" ),
    path('rechercheform',rechercheform, name="rechercheform" ),
    url(r'^details/(?P<details_id>[0-9]+)$', details, name='details'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

