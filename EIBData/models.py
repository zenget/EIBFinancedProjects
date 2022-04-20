from django.db import models
from django.conf import settings
    
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Country(TimeStampedModel):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.code

class Sector(TimeStampedModel):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.code

class FinancedProject(TimeStampedModel):
    signature_date = models.DateField()
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    signed_amount = models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self):
        return self.title