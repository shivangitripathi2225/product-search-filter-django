from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(blank=True, null= True)

    def __str__(self):
        return self.name
    
