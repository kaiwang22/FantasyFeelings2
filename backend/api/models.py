from django.db import models

# Create your models here.
class NFLPlayer(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=2)
    team = models.CharField(max_length=100)
    current_feeling = models.FloatField(default = 0.0)

class SentimentEntry(models.Model):
    player = models.ForeignKey(NFLPlayer, on_delete=models.CASCADE, related_name='sentiment_entries')
    title = models.CharField(max_length= 1000)
    times = models.DateTimeField(default=None, null=True, blank=True)
    score = models.FloatField()
