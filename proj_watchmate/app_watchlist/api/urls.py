from django.urls import path, include
#from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import (WatchListAV, WatchDetailsAV, StreamPlatformListAV,
                                     StreamDetailAV, ReviewList, ReviewDetail, ReviewCreate,
                                     UserReview, WatchList)

urlpatterns = [
    #path('list/', WatchListAV.as_view(), name="watch-list"),
    path('new-list/', WatchList.as_view(), name='new-list'),
    path('<int:pk>/', WatchDetailsAV.as_view(), name="movie-detail"),
    path('stream/', StreamPlatformListAV.as_view()),
    path('stream/<int:pk>', StreamDetailAV.as_view()),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name="review-create"),
    path('<int:pk>/review/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-id"),
    #path('review/<str:username>/', UserReview.as_view(), name="user-review")
    # ,
    path('review/', UserReview.as_view(), name="user-review"),

]   