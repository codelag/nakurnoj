from django.db import models
from datetime import datetime

# clients, contacts, payers
class Contact(models.Model):
    
    full_name = models.CharField(max_length=200, blank=True)
    position = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.full_name


class Payer(models.Model):

    company_name = models.CharField(max_length=200, blank=True)
    contract_num = models.CharField(max_length=20, blank=True)
    contract_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.company_name


class Invoice(models.Model):

    invoice_num = models.CharField(max_length=20, blank=True)
    invoice_date = models.DateField(default=datetime.now)
    payer_id = models.ForeignKey(Payer, on_delete=models.DO_NOTHING)
    price = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.invoice_date} ({self.is_paid})'


class Client(models.Model):
 
    company_name = models.CharField(max_length=200, blank=True)
    contact_id = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)
    payer_id = models.ForeignKey(Payer, on_delete=models.DO_NOTHING)
    post_addr = models.CharField(max_length=1000, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.company_name