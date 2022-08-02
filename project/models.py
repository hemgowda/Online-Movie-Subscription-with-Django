import email
from django.db import models

# Create your models here.
 
class Director(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    company = models.CharField(max_length=60)
    language = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
 
class Actor(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=50)
    language = models.CharField(max_length=60)
    rating = models.IntegerField()
    def __str__(self):
        return self.name
    
 
class customer(models.Model):
    name = models.CharField(max_length=30)
    passward = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    lamguage = models.CharField(max_length=100)
    year = models.IntegerField()
    Director = models.ForeignKey(Director, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    
    
class Book(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    date = models.DateField()
    show=models.TimeField()
    def __str__(self):
        return self.movie
    
class casting(models.Model):
    
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    time=models.TimeField()
    role = models.CharField(max_length=100)
    def __str__(self):
        return self.date
