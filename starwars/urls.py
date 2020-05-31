from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/films/', permanent=True)),
    path('films/', include('films.urls')),
] 

