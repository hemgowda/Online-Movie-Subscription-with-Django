
from django.contrib import admin
from project.models import Actor,customer,Movie,casting,Director,Book

# Register your models here.
@admin.register(Director)
class directorAdmin(admin.ModelAdmin):
    list_display = ('name','company')
    ordering = ('name',)
    search_fields = ('name','company')
    list_filter = ('name', 'company')
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name','rating')
    ordering = ('name',)
    search_fields = ('name','rating')
    list_filter = ('name', 'rating')
    
@admin.register(customer)
class customer(admin.ModelAdmin):
    list_display = ('name','email')
    ordering = ('name',)
    search_fields = ('name','email')
    list_filter = ('name', 'email')
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','year')
    #ordering = ('name')
    search_fields = ('name','year')
    list_filter = ('name', 'year')
   

admin.site.register(Book)
    
    

admin.site.register(casting)
