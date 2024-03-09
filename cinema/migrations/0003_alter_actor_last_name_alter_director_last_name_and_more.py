# Generated by Django 5.0.3 on 2024-03-08 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_remove_actor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='cinema.genre'),
        ),
    ]
