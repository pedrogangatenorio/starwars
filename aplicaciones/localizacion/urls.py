from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'localizacion'

urlpatterns = [
	path('', Contacto.as_view(), name='contacto'),
	]    