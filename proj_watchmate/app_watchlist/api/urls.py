from django.urls import path, include
#from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import (WatchListAV, WatchDetailsAV, StreamPlatformListAV,
                                     StreamDetailAV, ReviewList, ReviewDetail, ReviewCreate)

urlpatterns = [
    path('list/', WatchListAV.as_view()),
    path('<int:pk>/', WatchDetailsAV.as_view(), name="movie-detail"),
    path('stream/', StreamPlatformListAV.as_view()),
    path('stream/<int:pk>', StreamDetailAV.as_view()),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name="review-create"),
    path('<int:pk>/review/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-id"),

]   