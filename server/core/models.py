from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    Code = models.CharField(max_length=30)
    Eng_Name = models.CharField(max_length=30)
    Arb_Name = models.CharField(max_length=30)
    Remarks = models.CharField(max_length=50)
    Reg_Date = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)

class Branch(models.Model):
    Code = models.CharField(max_length=30)
    Eng_Name = models.CharField(max_length=30)
    Arb_Name = models.CharField(max_length=30)
    Remarks = models.CharField(max_length=50)
    Reg_Date = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)

class Chains(models.Model):
    Code = models.CharField(max_length=30)
    Eng_Name = models.CharField(max_length=30)
    Arb_Name = models.CharField(max_length=30)
    Remarks = models.CharField(max_length=50)
    Reg_Date = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)
