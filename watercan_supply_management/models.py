from django.db import models
import uuid
from django.contrib.auth.models import User
from authentication.models import *


class UserInfo(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null = True,blank =True)
    user_authentication = models.ForeignKey(UserAuthentication,on_delete=models.SET_NULL,null = True,blank = True)
    #name = models.CharField(max_length=200,null = True,blank=True)
    contact_number = models.CharField(max_length=10,null = True,blank=True)
    #email = models.EmailField(max_length=250,null=True,blank=True)
    address = models.TextField(blank=True,null=True)

    def __str__ (self):
        return f'{self.id}{self.user.first_name}'


class Watercan(BaseModel):
    brand = models.CharField(max_length=200,null = True,blank=True)
    size = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to = 'profile_pics/',null=True,blank=True)
    supplier = models.ForeignKey(UserInfo,on_delete = models.SET_NULL,null = True,blank = True)
    
    def __str__ (self):
        return f'{self.brand}=={self.id}'
    

# class Customer(BaseModel):
#    user = models.ForeignKey(User, on_delete=models.SET_NULL,null = True,blank =True)
#    #name = models.CharField(max_length=200,null = True,blank=True)
#    contact_number = models.CharField(max_length=10,null = True,blank=True)
#    #email = models.EmailField(max_length=250,null=True,blank=True)
#    address = models.TextField(blank=True,null=True)

#    def __str__ (self):
#      return f'{self.id}'





