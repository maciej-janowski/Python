# Generated by Django 3.0.4 on 2020-09-13 20:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20200913_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repair',
            name='product_provided',
        ),
        migrations.RemoveField(
            model_name='repair',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='repair',
            name='service_provided',
        ),
        migrations.RemoveField(
            model_name='repair',
            name='testing',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service',
        ),
        migrations.AddField(
            model_name='repair',
            name='plate',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='product_provided',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='service',
            name='repair',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car.Repair'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_provided',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='what_provided',
            field=models.CharField(choices=[('USŁUGA', 'USŁUGA'), ('CZĘŚĆ', 'CZĘŚĆ')], max_length=8, null=True),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
