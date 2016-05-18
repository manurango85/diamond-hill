from django.db import models

class daily_work(models.Model):
    date_time = models.DateField()
    number_plate = models.CharField(max_length=100)
    load_type = models.CharField(max_length=100)
    tonnes = models.IntegerField(default=0)
    trips = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    

    def __str__(self):

        return "%s" % self.customer_name

class customer(models.Model):
    date_time = models.DateField()
    customer_name = models.ForeignKey(daily_work)
    customer_id = models.IntegerField(default=0)
    amt_deposited = models.IntegerField(default=0)
    balance_amt = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.date_time
    
class employee(models.Model):
    date_time = models.DateField()
    employee_name = models.CharField(max_length=100)
    amt_paid = models.IntegerField(default=0)
    balance_amt = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.date_time
    
class repairs_maintanace(models.Model):
    date_time = models.DateField()
    mechanic_name = models.CharField(max_length=100)
    amt_paid = models.IntegerField(default=0)
    balance_amt = models.IntegerField(default=0)
    part_name = models.CharField(max_length=100)
    part_price = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.date_time
    
    



    

# Create your models here.
