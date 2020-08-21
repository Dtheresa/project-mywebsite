from django.shortcuts import render
from .models import Album


# Create your views here.
def song_list(request):
	country_songs = Album.objects.filter(genre__lte='Country')
	kpop_songs = Album.objects.filter(genre='K-pop')
	pop_songs =  Album.objects.filter(genre='Pop')
	rap_songs = Album.objects.filter(genre='Rap')
	return render(request, 'music/song_list.html', {'country_songs': country_songs, 'kpop_songs': kpop_songs, 'pop_songs': pop_songs, 'rap_songs': rap_songs})