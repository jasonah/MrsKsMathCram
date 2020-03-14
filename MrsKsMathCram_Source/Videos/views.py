from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Videos

class VideosListView(ListView):
    model = Videos

class VideosDetailView(DetailView):
    model = Videos