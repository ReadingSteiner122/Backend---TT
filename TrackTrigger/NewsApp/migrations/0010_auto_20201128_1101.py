# Generated by Django 3.1.3 on 2020-11-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0009_auto_20201128_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileotp',
            name='otp',
            field=models.CharField(default=308265, max_length=6),
        ),
    ]