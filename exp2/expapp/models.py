from django.db import models

# Create your models here.
class cinema(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cinema/')
    description = models.TextField()
    def __str__(self):
        return self.name
