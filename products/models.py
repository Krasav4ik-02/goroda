from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()
    city_id = models.IntegerField(null=True, blank=True)