from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key= True, default=uuid.uuid4,editable=False)
    class Meta:
        abstract = True

class Invoice(BaseModel):
    date = models.DateField()
    customer_name = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.date} == {self.id}'

class InvoiceDetail(BaseModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'{self.invoice.customer_name} === {self.id}'

  