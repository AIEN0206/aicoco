# Generated by Django 2.0.5 on 2018-05-30 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MemberCentre', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membercentre',
            name='annual_income',
        ),
    ]