# Generated by Django 5.0.1 on 2024-02-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pokeTracker', '0002_delete_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('natid', models.IntegerField(primary_key=True, serialize=False)),
                ('species', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('type1', models.CharField(max_length=255)),
                ('type2', models.CharField(blank=True, max_length=255, null=True)),
                ('altform', models.BooleanField()),
            ],
        ),
    ]
