# Generated by Django 3.1.4 on 2021-01-03 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betting_manager', '0009_auto_20210102_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchfinalstagerealeight',
            name='stage',
            field=models.CharField(choices=[('GROUP', 'GROUP'), ('BEST16', 'BEST16'), ('QF', 'QF'), ('SF', 'SF'), ('F', 'F')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='matchfinalstagerealfinal',
            name='stage',
            field=models.CharField(choices=[('GROUP', 'GROUP'), ('BEST16', 'BEST16'), ('QF', 'QF'), ('SF', 'SF'), ('F', 'F')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='matchfinalstagerealfour',
            name='stage',
            field=models.CharField(choices=[('GROUP', 'GROUP'), ('BEST16', 'BEST16'), ('QF', 'QF'), ('SF', 'SF'), ('F', 'F')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='matchfinalstagerealsixteen',
            name='stage',
            field=models.CharField(choices=[('GROUP', 'GROUP'), ('BEST16', 'BEST16'), ('QF', 'QF'), ('SF', 'SF'), ('F', 'F')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='matchgroupstagereal',
            name='stage',
            field=models.CharField(choices=[('GROUP', 'GROUP'), ('BEST16', 'BEST16'), ('QF', 'QF'), ('SF', 'SF'), ('F', 'F')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='matchfinalstagebettingeight',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='betting_manager.matchfinalstagerealeight'),
        ),
        migrations.AlterField(
            model_name='matchfinalstagebettingfinal',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='betting_manager.matchfinalstagerealfinal'),
        ),
        migrations.AlterField(
            model_name='matchfinalstagebettingfour',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='betting_manager.matchfinalstagerealfour'),
        ),
        migrations.AlterField(
            model_name='matchfinalstagebettingsixteen',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='betting_manager.matchfinalstagerealsixteen'),
        ),
    ]
