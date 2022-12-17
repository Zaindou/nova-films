from rest_framework import routers
from movies_app import viewset


router = routers.DefaultRouter()

router.register('api/movies', viewset.MovieViewSet, 'movies')
router.register('api/movie/random', viewset.RandomMovieVieSet, 'random_movie')

urlpatterns = router.urls