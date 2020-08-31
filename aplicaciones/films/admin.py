from django.contrib import admin
from .models import Film, Character, CharacterImage, Score, Comment, Like

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title','director','producer',)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(CharacterImage)
class CharacterImageAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('usuario','puntuacion',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('usuario','fecha', 'texto',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('usuario','fecha',)