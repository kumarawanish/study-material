from django.db import models
# Create your models here.

class MyModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
  
    def __str__(self):
        return self.title
    
class Student(models.Model):
    stuid = models.IntegerField()
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
