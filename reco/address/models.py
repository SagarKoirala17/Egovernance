from django.db import models
from pages.models import Citizen
ADDRESS_CHOICES = (
    (0, 'Permanent'),
    (1, 'Temporary'),

)

# Create your models here.
class Address(models.Model):
    citizen=models.ForeignKey(Citizen,on_delete=models.CASCADE)
    zone=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    village=models.CharField(max_length=30)
    ward = models.CharField(max_length=10)
    tole = models.CharField(max_length=30)
    village = models.CharField(max_length=30)
    house_no = models.CharField(max_length=30)
    address_type = models.IntegerField(choices=ADDRESS_CHOICES,default=0)

    def __str__(self):
        return self.zone




