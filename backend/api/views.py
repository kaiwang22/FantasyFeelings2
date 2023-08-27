from django.shortcuts import render
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NFLPlayer, SentimentEntry
from scrape import scrape_news
from .serializers import NFLPlayerSerializer, SentimentEntrySerializer
import datetime

# Create your views here.
class PlayerList(APIView):
    def get(self, request):
        players = NFLPlayer.objects.all()
        serializer = NFLPlayerSerializer(players, many=True)
        return Response(serializer.data)

class PlayerSearch(APIView):
    def get(self, request):
        search_query = request.query_params.get('search', '')
        players = NFLPlayer.objects.filter(name__icontains=search_query)
        serializer = NFLPlayerSerializer(players, many=True)
        return Response(serializer.data)

class PlayerDetail(APIView):
    def get(self, request, player_id):
        try:
            player = NFLPlayer.objects.get(pk=player_id)
        except NFLPlayer.DoesNotExist:
             return Response({"message": "Player not found"}, status=404)
        
        current_datetime = datetime.datetime.now(datetime.timezone.utc)
        recent = current_datetime - datetime.timedelta(days=3)
        recent_entries = SentimentEntry.objects.filter(player=player, times__gt=recent)
        mean_current_sentiment = recent_entries.aggregate(avg_score=Avg('score'))['avg_score']

        if mean_current_sentiment is not None:
            NFLPlayer.objects.filter(pk=player_id).update(current_feeling=mean_current_sentiment)
        

        serializer = NFLPlayerSerializer(player)
        return Response(serializer.data)

class PlayerSentimentView(APIView):
    def get(self, request, player_id):
        try:
            player = NFLPlayer.objects.get(id=player_id)
        except NFLPlayer.DoesNotExist:
            return Response({"message": "Player not found"}, status=404)
        
        sentiment_entries = SentimentEntry.objects.filter(player=player)
        serializer = SentimentEntrySerializer(sentiment_entries, many=True)
        return Response(serializer.data)

    def post(self, request, player_id):
        player = get_object_or_404(NFLPlayer, id=player_id)

        most_recent_entry = SentimentEntry.objects.filter(player=player).order_by('-times').first()
        if most_recent_entry:
            recent_datetime = most_recent_entry.times
        else:
            recent_datetime = None
        
        existing_titles = SentimentEntry.objects.filter(player=player).values_list('title', flat=True)
        
        new_articles = scrape_news(player.name)

        new_entries = []
        for index, article in new_articles.iterrows():
            if recent_datetime is None or article['Times'] > recent_datetime:
                entry_title = article['Titles']
                if entry_title not in existing_titles:
                    new_entries.append(SentimentEntry(player=player, title=entry_title, times=article['Times'], score=article['Score']))

        if new_entries:
            SentimentEntry.objects.bulk_create(new_entries)

        return Response({"message": f"{len(new_entries)} new articles added to sentiment entries."})

        #new_articles = scrape_news(player.name)
       # existing_titles = SentimentEntry.objects.filter(player=player).values_list('title', flat=True)

       # for index, article in new_articles.iterrows():
        #    if article['Titles'] not in existing_titles:
        #        SentimentEntry.objects.create(player=player, title=article['Titles'], times=article['Times'], score=article['Score'])
       # return Response({"message": "New articles added to sentiment entries."})


        