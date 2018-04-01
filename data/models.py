from django.db import models

# Create your models here.
class AddTruck(models.Model):
    truck_number = models.CharField(max_length=10,null=False,blank=False)
    insurance_date = models.DateField(null=False,blank=False)
    fitness_date= models.DateField(null=False,blank=False)
    pollution_date = models.DateField(null=False, blank=False)

class Notification(models.Model):
    truck_number = models.CharField(max_length=10,null=False,blank=False)
    insurance_date = models.DateField(null=False,blank=False)
    fitness_date= models.DateField(null=False,blank=False)
    pollution_date = models.DateField(null=False, blank=False)
    remaining_insurance= models.IntegerField(null=False,blank=False)
    remaining_fitness= models.IntegerField(null=False,blank=False)
    remaining_pollution= models.IntegerField(null=False,blank=False)
    remainder= models.IntegerField(default=31)
    read=models.BooleanField(default=False)
    remainded_day_insurane = models.IntegerField(default=31)
    remainded_day_fitness = models.IntegerField(default=31)
    remainded_day_pollution = models.IntegerField(default=31)