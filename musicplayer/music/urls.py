from django.urls import path
from .views import song_list, play_song

urlpatterns = [
    path('', song_list, name='song_list'),
    path('play/<int:song_id>/', play_song, name='play_song'),
]
