# Generated by Django 5.0.1 on 2024-03-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeTracker', '0008_shinydexcheckedcheckbox_checked_checkboxes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='link',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]