from django.db import models as mo
from datetime import date
# Create your models here.
class feeds(mo.Model):
    fid=mo.CharField(max_length=100,default='',primary_key=True)
    category=mo.CharField(max_length=100,default='')
    title=mo.CharField(max_length=100,default='')
    subtitle=mo.CharField(max_length=200,default='')
    desc=mo.TextField(max_length=10000,default='')
    time=mo.DateField(default=date.today())

    def __str__(self):
        return self.fid