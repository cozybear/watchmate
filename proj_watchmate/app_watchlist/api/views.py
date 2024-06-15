from rest_framework.response import Response
from rest_framework import status, generics, mixins
from app_watchlist.models import WatchList, StreamPlatform, Review
from rest_framework.views import APIView
from app_watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
#from rest_framework.decorators import api_view


class ReviewCreate(generics.CreateAPIView):
    """ View for adding a new review"""
    
    serializer_class = ReviewSerializer
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=movie)

class ReviewList(generics.ListAPIView):
    """ Get all reviews for specific watchlist item"""
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """ View For retrieving updating or deleting a specific event."""
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

class StreamPlatformListAV(APIView):
    
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
