from django.core.management.base import BaseCommand
from api.models import NFLPlayer, SentimentEntry
from datetime import datetime, timedelta
from django.utils import timezone
from api.views import scrape_news

class Command(BaseCommand):
    help = 'Populate sentiment entries for all NFL players'

    def handle(self, *args, **options):
        players = NFLPlayer.objects.all()

        for player in players:
            new_articles = scrape_news(player.name)
            existing_titles = SentimentEntry.objects.filter(player=player).values_list('title', flat=True)

            for index, article in new_articles.iterrows():
                if article['Titles'] not in existing_titles:
                    SentimentEntry.objects.create(player=player, title=article['Titles'], times=article['Times'], score=article['Score'])
        
        self.stdout.write(self.style.SUCCESS('Successfully populated sentiment entries.'))
