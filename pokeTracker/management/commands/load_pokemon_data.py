# class_projects/pokeTracker/management/commands/load_pokemon_data.py
from django.core.management.base import BaseCommand
from django.contrib.staticfiles import finders
from pokeTracker.models import Pokemon
import csv

class Command(BaseCommand):
    help = 'Load initial Pokemon data'

    def handle(self, *args, **options):
        csv_path = finders.find('info_db.csv')

        if not csv_path:
            self.stderr.write(self.style.ERROR('CSV file not found'))
            return

        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Pokemon.objects.create(
                    natid=row['natid'],
                    species=row['species'],
                    region=row['region'],
                    type1=row['type1'],
                    type2=row['type2'],
                    altform=row['altform'] == 'True',
                    link=row['link']
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded Pokemon data'))
