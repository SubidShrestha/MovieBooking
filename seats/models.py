from django.db import models
from users.models import user
from movies.models import movie

class seat(models.Model):
    seat_code=models.CharField(max_length=5,null=True)
    booking=models.BooleanField(default=False)
    price=models.IntegerField(default=200)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.seat_code

class bookedseat(models.Model):
    seat=models.ForeignKey(seat,on_delete=models.CASCADE,null=True,related_name='book')
    movie=models.ForeignKey(movie,on_delete=models.CASCADE,null=True,related_name='bookmovie')
    customer=models.ForeignKey(user,on_delete=models.CASCADE,null=True,related_name='bookuser')
    movie_date=models.DateField(null=True)
    movie_time=models.TimeField(null=True)
    booked_date=models.DateField(auto_now_add=True)
    booked_time=models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.seat.seat_code
