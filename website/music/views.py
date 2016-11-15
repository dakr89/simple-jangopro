from django.shortcuts import render
from django.http import HttpResponse
from  django.template import loader
from  .models import Album

def index(request):
	all_albums = Album.objects.all()
	html = ''
	template = loader.get_template('music/index.html')
	context = {
	'all_albums': all_albums,
	}
	return HttpResponse(template.render(context,request))

def details(request,album_id):
	return HttpResponse("<h2>Details for album_id: "+str(album_id)+ "</h2>")
