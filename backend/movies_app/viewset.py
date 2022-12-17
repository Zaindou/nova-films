from .models import Movie, Rating, User
from rest_framework import viewsets, permissions
from .serializer import MovieSerializer, UserSerializer, RatingSerializer
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('?')
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'genero', 'tipo']
    permission_classes = [
        permissions.AllowAny     
    ]
    serializer_class = MovieSerializer

    @action(detail=True, methods=['post'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print(stars, movie, user)
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RandomMovieVieSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('?')[:1]
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MovieSerializer





    



