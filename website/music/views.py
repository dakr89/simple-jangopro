from django.shortcuts import render,get_object_or_404
from  django.shortcuts import render
from  .models import Album

#  music index page function
def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', {'all_albums': all_albums})

# details about album function
def details(request,album_id):
	# try:
	# 	album = Album.objects.get(pk=album_id)
	# except:
	# 	raise Http404("Album Doesnot Exist")
	#  instead of writing 404 again and again use builtin get_objecct_or_404 

	album = get_object_or_404(Album,pk=album_id)
	return render(request, 'music/details.html', {'album':album})


def faviroute(request,album_id):
	album = get_object_or_404(Album,pk=album_id)
	try:
		selected_song = album.songs_set.get(pk=request.POST['song'])
	except(KeyError):
		return render(request, 'music/details.html', {'album':album, 'error_message':'Select Some Thing'})
	else:
		selected_song.is_faviroute = True
		selected_song.save()
		return render(request, 'music/details.html', {'album':album})