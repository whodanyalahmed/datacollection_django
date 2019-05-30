from django.db import models

# Create your models here.

class personal_data(models.Model):
    name = models.CharField(max_length=244)
    fathername = models.CharField(max_length=244)
    address = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(blank=True)
    ph = models.IntegerField()

    def __str__(self):
        return self.name[:15]