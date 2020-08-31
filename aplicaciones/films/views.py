import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from aplicaciones.films.mixins import LoginMixin
from .services import filmservice
from .models.film import Film
from .models.score import Score
from .models.comment import Comment
from .models.characterImage import CharacterImage
from .models.like import Like
from .filters.filters import FilmFilter
from aplicaciones.films.forms import FilmForm, FormularioLogin, ScoreForm, CommentForm

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('films:listado_films')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

class Logout(generic.View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('films:listado_films')

class FilmListView(generic.ListView):
    model = Film
    template_name = 'films/film_list.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['filter'] = FilmFilter(self.request.GET, queryset=self.get_queryset());
        context['images'] = CharacterImage.objects.all();
        context['carrusel_size'] = context['images'].order_by('id').values_list('id', flat=True);
        return context

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())

class ActualizarFilm(SuccessMessageMixin, generic.UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/film.html'
    success_url = reverse_lazy('films:listado_films')
    success_message = "Film was updated successfully"

class EliminaFilm(generic.DeleteView):
    model = Film

    def post(self,request,pk,*args,**kwargs):
        object = Film.objects.get(id = pk)
        object.delete()
        return redirect('films:listado_films')

class FilmDetailView(FormView, generic.DetailView):
    model = Film
    form_class = CommentForm
    template_name = 'films/film_detail.html'

    def get(self, *args, **kwargs):
        film = Film.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(initial={'usuario':self.request.user})
        return render(self.request,self.template_name,{'form':form,'film':film })
    
    def post(self,request,pk,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            film = Film.objects.get(pk=pk)
            film.comment.add(obj)
            film.save()
        return redirect('/films/' + str(pk))

class deleteComment(LoginMixin, generic.DeleteView):
    model = Comment
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        comment = Comment.objects.get(pk=pk)
        comment.estado = False
        comment.save()
        return redirect('/films/' + str(self.kwargs['pk1']))

class AddLike (LoginMixin, generic.TemplateView):
    model = Comment

    def get(self, request, *args, **kwargs):
        like = Like(usuario=self.request.user)
        like.save()
        pk = self.kwargs['pk']
        comment = self.model.objects.get(pk=pk)
        comment.like.add(like)
        comment.save()
        return redirect('/films/' + str(self.kwargs['pk1']))


class SessionsHistory(generic.TemplateView):
    model = Film

    def get_queryset(self):
        return self.model.objects.all()

    def get(self,request,*args,**kwargs):
        sessions = {}
        attrs = ['title', 'director', 'producer']
        for attr in attrs:
            sessions[attr] = list(self.get_queryset().values_list(attr, flat=True).distinct())
        return HttpResponse(json.dumps(sessions), content_type="application/json")

class CreateScore (LoginMixin, generic.CreateView):
    model = Score
    form_class = ScoreForm
    template_name = 'films/film_score.html'

    def get(self, *args, **kwargs):
        film = Film.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(initial={'usuario':self.request.user})
        return render(self.request,self.template_name,{'form':form,'film':film })

    def post(self,request,pk,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            film = Film.objects.get(pk=pk)
            film.score.add(obj)
            film.save()
        return redirect('films:listado_films')




