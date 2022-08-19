from django.db import models

# Create your models here.

class NoteLenovo(models.Model):
   name = models.CharField(max_length=100, )
   description = models.CharField(max_length=100)
   price = models.DecimalField(max_digits=6, decimal_places=2)
   
   class Meta:
    index_together = [
        ["name", "description"],
    ]