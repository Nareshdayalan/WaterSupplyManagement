from django.db import models
from watercan_supply_management.models import Watercan,UserInfo
from authentication.models import BaseModel


# Create your models here.
class Order(BaseModel):
    date_ordered = models.DateTimeField(null= True,blank=True)
    total_amount = models.IntegerField(default=1)
    is_completed = models.BooleanField(default=True)
    watercan_info = models.ManyToManyField(Watercan)

    def __str__(self):
        return f'{self.date_ordered}==={self.id}'


class Payment(BaseModel):
    amount = models.IntegerField(default=1)
    date_paid = models.DateTimeField(null= True,blank=True)
    customer = models.ForeignKey(UserInfo,on_delete = models.SET_NULL,null = True,blank=True)
    order = models.ForeignKey(Order,on_delete = models.SET_NULL,null = True,blank=True)
    
    def __str__(self):
        return f'{self.date_paid} == {self.id}'