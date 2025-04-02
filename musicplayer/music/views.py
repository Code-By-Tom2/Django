from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

def play_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return JsonResponse({'url': song.file.url})
