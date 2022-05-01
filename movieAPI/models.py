from django.db import models
from sqlalchemy import true

class Movie(models.Model):
    id = models.IntegerField(primary_key=true)
    title = models.CharField(max_length=50)
    vote_average = models.FloatField()
    local_rating = models.FloatField(null=True)
    
