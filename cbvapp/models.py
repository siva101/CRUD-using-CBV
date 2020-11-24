from django.db import models
from django.urls import reverse

class Student(models.Model):
    Fname=models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    Score = models.FloatField()

    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})