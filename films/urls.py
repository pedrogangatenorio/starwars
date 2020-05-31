from django.urls import path
from . import views

urlpatterns = [
	path('', views.FilmListView.as_view(), name='films'),
	path('<int:pk>', views.FilmDetailView.as_view(), name='film-detail'),
	path('getSession', views.getSession, name='getSession'),
	]    
