from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class MovieListView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

# Create your views here.




