from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(null=True, blank=True)
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'Review for {self.movie.title}'