# Generated by Django 5.1.4 on 2024-12-19 12:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_alter_player_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='role',
            field=models.CharField(choices=[('anchor', 'ANCHOR'), ('slayer', 'SLAYER'), ('supporter', 'SUPPORTER'), ('objective', 'OBJECTIVE')], default='objective', max_length=9),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('ongoing', 'Ongoing'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=10)),
                ('team_a_score', models.PositiveIntegerField(default=0)),
                ('teame_b_score', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_created', to=settings.AUTH_USER_MODEL)),
                ('team_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_team_a', to='team.team')),
                ('team_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_team_b', to='team.team')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_won', to='team.team')),
            ],
        ),
    ]