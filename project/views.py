from django.shortcuts import render

# Create your views here.
from django.views import generic
from project.models import Director,Actor,Movie,casting

class DirectorListView(generic.ListView):
    model = Director
    template_name = 'director_list.html'

class ActorListView(generic.ListView):
    model = Actor
    template_name = 'actor_list.html'
    
class movieListView(generic.ListView):
    model = Movie
    template_name = 'movie_list.html'
    
class castingListView(generic.ListView):
    model = casting
    template_name = 'casting_list.html'
    
