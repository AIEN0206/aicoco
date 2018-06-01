from django.db import models

# Create your models here.

# class Consultant(models.Model):
#     姓名 = models.CharField(max_length=20,null=False)
#     學歷 = models.CharField(max_length=100,null=False)
#     經歷 = models.CharField(max_length=100,null=False)
#     證照 = models.CharField(max_length=100,null=False)
    
#     class Meta:
#         db_table = "consultants"

class Consultant(models.Model):
    姓名 = models.CharField(max_length=20)
    學歷 = models.CharField(max_length=100)
    經歷 = models.CharField(max_length=100)
    證照 = models.CharField(max_length=100)
    image = models.CharField(max_length=45, blank=True, null=True)
    操盤特色 = models.CharField(max_length=500)
    url = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'consultants'