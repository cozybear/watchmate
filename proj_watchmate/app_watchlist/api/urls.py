from django.urls import path, include
from app_watchlist.api.views import movie_list, movie_details

urlpatterns = [
    path('list/', movie_list),
    path('<int:pk>', movie_details)

]