from django.db import models

# Create your models here.

class Consultant(models.Model):
    姓名 = models.CharField(max_length=20,null=False)
    學歷 = models.CharField(max_length=100,null=False)
    經歷 = models.CharField(max_length=100,null=False)
    證照 = models.CharField(max_length=100,null=False)
    
    class Meta:
        db_table = "consultants"