from django.db import models
import re
import vimeo

client = vimeo.VimeoClient(
  token='101cc19b08e333d78e17fe1c3e8f45d7',
  key='92bcc63acb140e48a348db92f42ffe2a26168942',
  secret='clqedoUebehQOvfbBBu58S2XYKMXzP7C2OgZ41icqHesmK47ITyDPDDeQcSF8E6uyUqNoYReA9JnawqFww8PfdDnsdaZfhEnmmtcWUlcTcOtXNrwYKJHtcB3Fgr8hdSU'
)

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Videos(models.Model):
    title = models.CharField(max_length=120, default='NULL')
    video_url = models.CharField(max_length=200, default='NULL')

    def __str__(self):
        return self.title

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