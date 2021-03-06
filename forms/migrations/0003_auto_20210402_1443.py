# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-02 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20210401_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercialvehicle',
            name='YOM',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='commercialvehicle',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='commercialvehicle',
            name='cover_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='commercialvehicle',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='commercialvehicle',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='commercialvehicle',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='commercialvehicle',
            name='registration_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='commercialvehicle',
            name='vehicle_make',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='commercialvehicle',
            name='vehicle_model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='cover_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='privatemotor',
            name='YOM',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='privatemotor',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='privatemotor',
            name='cover_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='privatemotor',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='privatemotor',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='privatemotor',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='privatemotor',
            name='registration_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='privatemotor',
            name='vehicle_make',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='privatemotor',
            name='vehicle_model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='psv',
            name='YOM',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='psv',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='psv',
            name='cover_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='psv',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='psv',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='psv',
            name='passengers',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='psv',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='psv',
            name='registration_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='psv',
            name='vehicle_make',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='psv',
            name='vehicle_model',
            field=models.CharField(max_length=50),
        ),
    ]
