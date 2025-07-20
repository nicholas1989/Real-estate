from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    price = models.IntegerField()
    square_footage = models.IntegerField()
    num_rooms = models.IntegerField()
    # image
    
    
    def __str__(self):
        return self.title
    