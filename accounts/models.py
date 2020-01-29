from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    part = models.Charfield(max_length=40)
    summary = models.CharField(max_length=240)
    description = models.TextField(max_length=1000, blank=False)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.title