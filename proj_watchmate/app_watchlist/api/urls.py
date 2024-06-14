from django.urls import path, include
#from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path('list/', MovieListAV.as_view()),
    path('<int:pk>', MovieDetailsAV.as_view())

]