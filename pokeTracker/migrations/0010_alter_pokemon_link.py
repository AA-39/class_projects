# Generated by Django 5.0.1 on 2024-03-28 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeTracker', '0009_pokemon_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
