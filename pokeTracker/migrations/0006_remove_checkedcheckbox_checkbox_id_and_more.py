# Generated by Django 5.0.1 on 2024-03-17 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeTracker', '0005_alter_checkedcheckbox_checkbox_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkedcheckbox',
            name='checkbox_id',
        ),
        migrations.AddField(
            model_name='checkedcheckbox',
            name='checked_checkboxes',
            field=models.TextField(default='[]'),
        ),
    ]
