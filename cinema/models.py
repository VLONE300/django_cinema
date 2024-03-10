from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='directors/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    image = models.ImageField(upload_to='movies/')

    def display_genre(self):
        return ','.join([genre.name for genre in self.genre.all()])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"movie_id": self.pk})


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.movie.title} at {self.date}"


class Ticket(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.IntegerField()

    def __str__(self):
        return f"Ticket for {self.show.movie.title} at {self.show.date} by {self.user.username}"

