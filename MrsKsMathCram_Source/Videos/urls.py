from django.urls import path
from .views import VideosListView, VideosDetailView

app_name = 'Videos'

urlpatterns = [
    path('', VideosListView.as_view(), name='list'),
    path('<slug>', VideosDetailView.as_view(), name='detail'),
]

