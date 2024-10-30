from django.db import models

class DistanceCalculation(models.Model):
    start_address = models.CharField(max_length=255)
    end_address = models.CharField(max_length=255)
    distance_km = models.DecimalField(max_digits=10, decimal_places=2)
    calculation_time = models.DateTimeField(auto_now_add=True)