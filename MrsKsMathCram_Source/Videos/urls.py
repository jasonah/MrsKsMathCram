from django.urls import path
from .views import VideosListView, VideosDetailView, VideoIndView

app_name = 'Videos'

urlpatterns = [
    path('', VideosListView.as_view(), name='list'),
    path('<slug>', VideosDetailView.as_view(), name='detail'),
    path('<ind_vid_slug>', VideoIndView.as_view(), name='individual-video')
]

