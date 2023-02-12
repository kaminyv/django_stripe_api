"""
API application models module
"""
from django.db import models
from django.urls import reverse


class Item(models.Model):
    """
    Model represents products
    """
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.FloatField()

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular item instance.
        """
        return reverse('item-detail', args=[str(self.id)])
