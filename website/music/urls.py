from django.conf.urls import url
from . import views
app_name = 'music'
urlpatterns = [
# /music/
    url(r'^$', views.index, name='index'),
# /music/81/
url(r'^(?P<album_id>[0-9]+)/$',views.details,name="details"),
# /music/81/favourite
url(r'^(?P<album_id>[0-9]+)/faviroute/$',views.faviroute,name="faviroute"),
]

