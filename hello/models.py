from django.db import models

# Create your models here.
class Item(models.Model):
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    