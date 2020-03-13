from django.db import models
from Memberships.models import Membership

class Videos(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Membership)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200) #Later on change this to a video hosting service like amazon aws or vimeo
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
    


