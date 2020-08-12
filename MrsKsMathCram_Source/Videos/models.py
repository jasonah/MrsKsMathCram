from django.db import models
from Memberships.models import Membership
from django.urls import reverse
import re
import vimeo

client = vimeo.VimeoClient(
  token='101cc19b08e333d78e17fe1c3e8f45d7',
  key='92bcc63acb140e48a348db92f42ffe2a26168942',
  secret='clqedoUebehQOvfbBBu58S2XYKMXzP7C2OgZ41icqHesmK47ITyDPDDeQcSF8E6uyUqNoYReA9JnawqFww8PfdDnsdaZfhEnmmtcWUlcTcOtXNrwYKJHtcB3Fgr8hdSU'
)

# response = client.get(uri)
# print(response.json())

class Videos(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Membership)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200) #Later on change this to a video hosting service like amazon aws or vimeo
    # thumbnail = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Videos:detail', kwargs={'slug': self.slug})

    @property
    def order_vids(self):
        return self.all().order_by('position') #This should make sure all videos are in order even if we go through and delete some
        
    def video_id(self):
        regex = r"vimeo\.com\/(\d+)"
        test_str = self.video_url
        matches = re.finditer(regex, test_str, re.IGNORECASE)
        for matchNum, match in enumerate(matches, start=1):
            # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                # print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
                return match.group(groupNum)