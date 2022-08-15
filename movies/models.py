from distutils.command.upload import upload
from django.db import models

class movie(models.Model):
    movie_name=models.CharField(max_length=255,null=False)
    banner=models.ImageField(upload_to='media/movies/',null=True)
    trailer=models.URLField(max_length=255,null=True)
    genre=models.CharField(max_length=20)
    synposis=models.TextField()
    production=models.CharField(max_length=40)
    producer=models.CharField(max_length=40)
    director=models.CharField(max_length=40)
    released_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie_name

