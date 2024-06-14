from django.urls import path, include
#from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import WatchListAV, WatchDetailsAV, StreamPlatformListAV, StreamDetailAV

urlpatterns = [
    path('list', WatchListAV.as_view()),
    path('<int:pk>', WatchDetailsAV.as_view()),
    path('stream', StreamPlatformListAV.as_view()),
    path('stream/<int:pk>', StreamDetailAV.as_view())

]   