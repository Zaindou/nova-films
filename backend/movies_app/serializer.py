from rest_framework import serializers
from .models import Movie, Rating
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        exta_kwargs = {'password': {'required': True, 'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user

class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.StringRelatedField()
    class Meta:
        model = Movie
        fields = ('id', 'nombre', 'genero', 'tipo', 'numero_visuales', 'rating_average', 'rating')
        extra_kwargs = {'url': {'read_only': True}}


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'movie', 'stars')



