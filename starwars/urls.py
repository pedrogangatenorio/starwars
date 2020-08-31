from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path
from django.urls import include
from django.contrib.auth.decorators import login_required
from aplicaciones.films.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', include(('aplicaciones.films.urls','films'))),
    path('localizacion/', include(('aplicaciones.localizacion.urls','localizacion'))),
    path('', FilmListView.as_view(), name = 'films'),
    path('accounts/login/', Login.as_view(), name = 'login'),
    path('logout/', login_required(Logout.as_view()), name = 'logout'),
] 
