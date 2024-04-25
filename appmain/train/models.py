from django.db import models

# Create your models here.
class Topic_to_learn(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Tests_to_do(models.Model):
    title = models.CharField(max_length=200)
    answer = models.CharField(max_length=200, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title