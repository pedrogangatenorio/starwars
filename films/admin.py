from django.contrib import admin

# Register your models here.
from films.models import Film, Character, CharacterImage

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title','director','producer',);

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name',);
    
@admin.register(CharacterImage)
class CharacterImageAdmin(admin.ModelAdmin):
    list_display = ('nombre',);