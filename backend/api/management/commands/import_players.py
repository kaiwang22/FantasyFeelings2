from django.core.management.base import BaseCommand
import pandas as pd
from api.models import NFLPlayer

class Command(BaseCommand):
    help = 'Imports current NFL player data from a CSV file'

    def handle(self, *args, **options):
        df = pd.read_csv('/Users/kaiwang/Downloads/all_nfl_players.csv')

        for index, row in df.iterrows():
            NFLPlayer.objects.create(
                name=row['Players'],
                position=row['Positions'],
                team=row['Teams']
            )