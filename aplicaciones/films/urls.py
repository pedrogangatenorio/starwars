from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'films'

urlpatterns = [
	path('', views.FilmListView.as_view(), name='listado_films'),
	path('<int:pk>', views.FilmDetailView.as_view(), name='film-detail'),
	path('editar_pelicula/<int:pk>', views.ActualizarFilm.as_view(), name='film-update'),
	path('eliminar_pelicula/<int:pk>', views.EliminaFilm.as_view(), name='film_delete'),
	path('<int:pk1>/add_like/<int:pk>', views.AddLike.as_view(), name='like_comment'),
	path('getSession', views.SessionsHistory.as_view(), name='getSession'),
	path('create_score/<int:pk>', views.CreateScore.as_view(), name='create_score'),
	path('<int:pk1>/delete_comment/<int:pk>', views.deleteComment.as_view(), name='delete_comment'),
	]    
