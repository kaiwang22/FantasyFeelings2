from django.urls import path
from .views import PlayerList, PlayerDetail, PlayerSentimentView, PlayerSearch

urlpatterns = [
    # Endpoint for getting a list of all players
    path('players/', PlayerList.as_view(), name='player-list'),

    path('players/search/', PlayerSearch.as_view(), name='player-search'),

    # Endpoint for getting details of a specific player and updating current feeling
    path('players/<int:player_id>/', PlayerDetail.as_view(), name='player-detail'),

    # Endpoint for getting sentiment entries for a specific player and adding new articles
    path('players/<int:player_id>/sentiment/', PlayerSentimentView.as_view(), name='player-sentiment'),
]
