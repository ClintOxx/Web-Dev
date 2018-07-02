from django.db import models

# Create your models here.
class Courses(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length= 255)
    description = models.TextField()

    def __str__(self):
        return self.title    

class Step(models.Model): # models
    title = models.CharField(max_length = 255) # attributes
    description = models.TextField()
    order = models.IntegerField(default = 0)
    course = models.ForeignKey(Courses)
    content = models.TextField(blank=True, default='')

    class Meta:
         ordering = ['order',]

    def __str__(self):
        return self.title # returns the title of the attributes 