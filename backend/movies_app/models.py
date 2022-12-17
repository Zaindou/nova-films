from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    numero_visuales = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.genero + " " + self.tipo

    def rating_average(self):
        ratings = Rating.objects.filter(movie=self)
        sum = 0
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField()

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)



