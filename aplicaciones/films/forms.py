from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models.film import Film
from .models.score import Score
from .models.comment import Comment
from .models.like import Like

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['usuario', 'puntuacion']
        labels = {
            'puntuacion': 'Puntuación'
        }

    def __init__(self, *args, **kwargs):
        initial_arguments = kwargs.get('initial', None)
        updated_initial = {}
        if initial_arguments:
            updated_initial['usuario'] = initial_arguments.get('usuario',None)
            kwargs.update(initial=updated_initial)
        super(ScoreForm, self).__init__(*args, **kwargs)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('usuario','texto',)
        labels = {
            'texto': ''
        }
        widgets = {
            'texto': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Write a comment...'
                }
            ),
            'usuario': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        initial_arguments = kwargs.get('initial', None)
        updated_initial = {}
        if initial_arguments:
            updated_initial['usuario'] = initial_arguments.get('usuario',None)
            kwargs.update(initial=updated_initial)
        super(CommentForm, self).__init__(*args, **kwargs)

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title','episode','description','director','producer','release_date', 'character']
        labels = {
            'title': 'Título de la película',
            'episode': 'Episodio',
            'description': 'descripción',
            'director': 'Director',
            'producer':'Productor',
            'release_date': 'Fecha Estreno'
        }
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del autor',
                    'id': 'nombre'
                }
            ),
            'episode': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los apellidos del autor',
                    'id':'apellidos'
                }
            ),
            'description': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese una pequeña descripcion para el autor',
                    'id':'descripcion'
                }
            ),
            'director': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese una pequeña descripcion para el autor',
                    'id':'descripcion'
                }
            ),
            'producer': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese una pequeña descripcion para el autor',
                    'id':'descripcion'
                }
            ),
            'release_date': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'character': forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            ),
        }
