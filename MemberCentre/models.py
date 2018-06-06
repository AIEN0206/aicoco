from django.db import models

# Create your models here.
class MemberCentre(models.Model):
    account = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45, blank=True, null=True)
    cellphone = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45)
    birth = models.DateField()
    address = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    education = models.CharField(max_length=45, blank=True, null=True)
    job = models.CharField(max_length=45, blank=True, null=True)
    grade = models.CharField(max_length=45)
    vcode = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membercentre'
