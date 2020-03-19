from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, View
from .models import Videos

class VideosListView(ListView):
    model = Videos

class VideosDetailView(DetailView):
    model = Videos

class VideoIndView(View):
    def get(self, request, ind_vid_slug, *args, **kwards): #Probs have to do some fiddling with this slug
        video_qs = Videos.objects.filter(slug=ind_vid_slug)
        if video_qs.exists():
            video = video_qs.first()
        
        context = {
            'object': video
        }

        return render(request, "videos_detail.html", context)

            
            