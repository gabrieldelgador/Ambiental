from django.db import models

# Create your models here. 
class Rios(models.Model):
    name=models.CharField(max_lenght=200)
    latitud=models.DecimalField(max_digits=9, decimal_places=6)
    logitud=models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self):
        return self.name