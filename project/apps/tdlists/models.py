from django.db import models
from datetime import datetime


# Create your models here.
class Tdlist(models.Model):

    task = models.TextField()
    cr_date = models.DateTimeField(default=datetime.now, blank=True)
    is_check = models.BooleanField(default=False)
    user_id = models.IntegerField()

    def __str__(self):
        return self.task
