from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('film/<int:filmid>/', categories), #http://127.0.0.1:8000/film/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]