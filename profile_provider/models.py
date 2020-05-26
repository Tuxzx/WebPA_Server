from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    introduction = models.TextField()
    background = models.TextField()
    looks = models.TextField()
    character = models.TextField()
    ability = models.TextField()
    weakness = models.TextField()
    extend = models.TextField()

class MessageBoard(models.Model):
    nickname = models.CharField(max_length=30)
    titleid = models.IntegerField()
    message = models.TextField()
    time = models.DateField()