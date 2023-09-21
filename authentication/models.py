from django.db import models
import uuid
from django.contrib.auth.models import User
# from watercan_supply_management.models import BaseModel

class BaseModel(models.Model):
    id = models.UUIDField(primary_key= True, default=uuid.uuid4,editable=False)
    class Meta:
        abstract = True
class UserAuthentication(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank = True)
    is_admin = models.BooleanField(default = False)
    is_employee = models.BooleanField(default = False)
    is_supplier = models.BooleanField(default = False)
    is_customer = models.BooleanField(default = False)
    mobile_otp = models.CharField(max_length = 5,null = True, blank = True)
