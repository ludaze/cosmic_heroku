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

class cosmic_order(models.Model):
    order_no = models.TextField(primary_key=True)
    #notify_party2 = models.ForeignKey('customer_profile', related_name='orders_related_to_bank', on_delete=models.CASCADE, db_column='notify_party2',blank=True, null=True)
    date = models.DateField(blank=False)
    payment_type = models.TextField(blank=True, null=True)
    measurement_type = models.TextField(blank=True, null=True)
    transportation = models.TextField(blank=True, null=True)
    shipment_type = models.TextField(blank=True, null=True)
    approved_by = models.TextField(blank=True, null=True)
    PR_before_vat = models.FloatField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, default="Pending")
    
class cosmic_purchase(models.Model):
    purchase_no = models.TextField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    measurement_type = models.TextField(blank=True, null=True)
    transportation = models.TextField(blank=True, null=True)
    shipment_type = models.TextField(blank=True, null=True)
    payment_type = models.TextField(blank=True, null=True)
    approved_by = models.TextField(blank=True, null=True)
    before_vat = models.FloatField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, default="Pending")

class shipping_info(models.Model):
    agreement = models.TextField(blank=True, null=True)
    PR_type = models.TextField(blank=True, null=True)
    unique_no = models.AutoField(primary_key=True)
    invoice_date = models.DateField(blank=True, null=True)
    port_of_loading = models.TextField(blank=False, null=True)
    port_of_discharge = models.TextField(blank=True, null=True)
    final_destination = models.TextField(blank=True, null=True)
    container_no = models.IntegerField(blank=True, null=True)
    truck_waybill_no = models.TextField(blank=True, null=True)
    country_of_origin = models.TextField(blank=False, null=True)
    customer_no = models.TextField(blank=True, null=True)
    freight_amount = models.FloatField(blank=True, null=True)
    