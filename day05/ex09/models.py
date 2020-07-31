from django.db import models
from django.utils import timezone


# Create your models here.
class movies(models.Model):
    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(unique=True, max_length=64, null=False, blank=False)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(null=False, blank=False, max_length=32)
    producer = models.CharField(null=False, blank=False, max_length=128)
    release_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    created = models.DateField(default=timezone.now)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Planets(models.Model):
    name = models.CharField(unique=True, null=False, max_length=64)
    climate = models.TextField()
    diameter = models.IntegerField()
    orbital_period = models.IntegerField()
    population = models.BigIntegerField()
    rotattion_period = models.IntegerField()
    suface_water = models.FloatField()
    terrain = models.TextField()

    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=64)
    birth_year = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
    eye_color = models.CharField(max_length=32)
    hair_color = models.CharField(max_length=32)
    height = models.IntegerField()
    mass = models.FloatField()
    homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE)

    def __str__(self):
        return self.name