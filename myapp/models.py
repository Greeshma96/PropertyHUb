from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.CharField(max_length=255)

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent = models.IntegerField()
    property_type = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK')
    ]
    unit_type = models.CharField(max_length=4, choices=property_type)

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    document_proofs = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.IntegerField()