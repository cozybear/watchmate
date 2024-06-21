from rest_framework.response import Response
from rest_framework import status, generics, mixins,  viewsets
from app_watchlist.models import WatchList, StreamPlatform, Review
from rest_framework.views import APIView
from app_watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from app_watchlist.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadonly
#from rest_framework.decorators import api_view


class ReviewCreate(generics.CreateAPIView):
    """ View for adding a new review"""
    
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()
    
    serializer_class = ReviewSerializer
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("You already reviewed this item")
        
        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2

        movie.number_rating += 1
        movie.save()
        serializer.save(watchlist=movie, review_user=review_user)

    

class ReviewList(generics.ListAPIView):
    """ Get all reviews for specific watchlist item"""
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """ View For retrieving updating or deleting a specific event."""
    permission_classes = [IsReviewUserOrReadonly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

    # def get_queryset(self):
    #     reviewid = int(self.args['reviewid'])
    #     return Review.objects.filter(id=reviewid)


# class ReviewDetail(mixins.RetrieveModelMixin,
#                     generics.GenericAPIView):
#     """ View for accessing specific review by review Id"""
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
    
#     """ View for listing all the reviews at once"""
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class StreamPlatformVS(viewsets.ViewSet):
    permission_classes = [IsAdminOrReadOnly]

    def list(self, request):
        
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(StreamPlatform)
        return Response(serializer.data)


class StreamPlatformListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamDetailAV(APIView):

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(platform)
            return Response(serializer.data)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Platform Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"Error": "Platform Not Found"}, status=status.HTTP_400_BAD_REQUEST)

        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Platform Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            platform.delete()
            return Response({"Action": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Platform Not Found"}, status=status.HTTP_404_NOT_FOUND)
        

class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            serializer.errors({"Error": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailsAV(APIView):
    """ Class For Movie Details"""
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            """ Function To Get Movie Item """
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
            
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors())    
            
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
    

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            movie = WatchList.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors())


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request,pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
    
#         if request.method == 'GET':
            
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)
        
#         if request.method == 'PUT':
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 serializer.errors()

#         if request.method == 'DELETE':
#             movie = Movie.objects.get(pk=pk)
#             movie.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
    
#     except Movie.DoesNotExist:
#         return Response({"Error": "Movie Not Found"}, status=status.HTTP_404_NOT_FOUND)
