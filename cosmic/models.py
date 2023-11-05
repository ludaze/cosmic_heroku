from django.db import models

# Create your models here.
class customer_profile(models.Model):
    #customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField(blank=True,primary_key=True)
    customer_address = models.TextField(blank=True)
    contact_person = models.TextField(blank=True)
    phone_number = models.CharField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

class supplier_profile(models.Model):
    #supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.TextField(primary_key=True)
    supplier_address = models.TextField(blank=True)
    contact_person = models.TextField(blank=True)
    phone_number = models.CharField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
