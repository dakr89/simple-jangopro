from django.http import Http404
from django.shortcuts import render
from  django.shortcuts import render
from  .models import Album

#  music index page function
def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', {'all_albums': all_albums})

# details about album function
def details(request,album_id):
	try:
		album = Album.objects.get(pk=album_id)
	except:
		raise Http404("Album Doesnot Exist")
	return render(request, 'music/details.html', {'album':album})
