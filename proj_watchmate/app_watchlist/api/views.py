
from rest_framework.response import Response
from rest_framework import status
from app_watchlist.models import Movie
from rest_framework.views import APIView
from app_watchlist.api.serializers import MovieSerializer

#from rest_framework.decorators import api_view


class MovieListAV(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serilizer = MovieSerializer(movies, many=True)
        return Response(serilizer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            serializer.errors({"Error": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsAV(APIView):
    """ Class For Movie Details"""
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            """ Function To Get Movie Item """
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
            
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors())    
            
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
    

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


        except Movie.DoesNotExist:
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
