# Generated by Django 3.1.4 on 2020-12-31 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betting_manager', '0007_remove_team_nailing'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchFinalStageRealSixteen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_team_one', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True)),
                ('goals_team_two', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True)),
                ('penalties_team_one', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('penalties_team_two', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('score_team_one', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('score_team_two', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('played', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True)),
                ('team_one', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_one_final_sixteen', to='betting_manager.team')),
                ('team_two', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_two_final_sixteen', to='betting_manager.team')),
            ],
        ),
        migrations.CreateModel(
            name='MatchFinalStageRealFour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_team_one', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True)),
                ('goals_team_two', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True)),
                ('penalties_team_one', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('penalties_team_two', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('score_team_one', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('score_team_two', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('played', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True)),
                ('team_one', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_one_final_four', to='betting_manager.team')),
                ('team_two', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_two_final_four', to='betting_manager.team')),
            ],
        ),
        migrations.CreateModel(
            name='MatchFinalStageRealFinal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_team_one', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True)),
                ('goals_team_two', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True)),
                ('penalties_team_one', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('penalties_team_two', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('score_team_one', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('score_team_two', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('played', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True)),
                ('team_one', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_one_final_championship', to='betting_manager.team')),
                ('team_two', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_two_final_championship', to='betting_manager.team')),
            ],
        ),
        migrations.CreateModel(
            name='MatchFinalStageRealEight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_team_one', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True)),
                ('goals_team_two', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True)),
                ('penalties_team_one', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('penalties_team_two', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('score_team_one', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('score_team_two', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('played', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True)),
                ('team_one', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_one_final_eight', to='betting_manager.team')),
                ('team_two', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_two_final_eight', to='betting_manager.team')),
            ],
        ),
        migrations.CreateModel(
            name='MatchFinalStageBettingSixteen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_team_one', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('goals_team_two', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('score_team_one', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('score_team_two', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('penalties_team_one', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('penalties_team_two', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('points', models.IntegerField(default=0)),
                ('checked', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True)),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='betting_manager.matchfinalstagerealsixteen')),
                ('person_betting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='betting_manager.player')),
            ],
        ),
        migrations.CreateModel(
            name='MatchFinalStageBettingFour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_team_one', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('goals_team_two', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('score_team_one', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('score_team_two', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('penalties_team_one', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('penalties_team_two', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('points', models.IntegerField(default=0)),
                ('checked', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True)),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='betting_manager.matchfinalstagerealfour')),
                ('person_betting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='betting_manager.player')),
            ],
        ),
        migrations.CreateModel(
            name='MatchFinalStageBettingFinal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_team_one', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('goals_team_two', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('score_team_one', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('score_team_two', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('penalties_team_one', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('penalties_team_two', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('points', models.IntegerField(default=0)),
                ('checked', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True)),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='betting_manager.matchfinalstagerealfinal')),
                ('person_betting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='betting_manager.player')),
            ],
        ),
        migrations.CreateModel(
            name='MatchFinalStageBettingEight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_team_one', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('goals_team_two', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('score_team_one', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('score_team_two', models.CharField(choices=[('WIN', 'WIN'), ('DEFEAT', 'DEFEAT')], max_length=6, null=True)),
                ('penalties_team_one', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('penalties_team_two', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=1, null=True)),
                ('points', models.IntegerField(default=0)),
                ('checked', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True)),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='betting_manager.matchfinalstagerealeight')),
                ('person_betting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='betting_manager.player')),
            ],
        ),
    ]
