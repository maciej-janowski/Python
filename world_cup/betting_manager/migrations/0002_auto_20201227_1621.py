# Generated by Django 3.1.4 on 2020-12-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betting_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchfinalstagereal',
            name='played',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='matchgroupstagereal',
            name='played',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True),
        ),
    ]
