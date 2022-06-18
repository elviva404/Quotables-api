from ast import IsNot
from unicodedata import category
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters

from quotables.models import User, Mood, Artist, Category, Quote
from .serializers import UserSerializer, QuoteSerializer, MoodSerializer, ArtistSerializer, CategorySerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


# Create your views here.

class UserEndpoint(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter)
    search_fields = ('name', 'email',)


class UserLoginEndpoint(ObtainAuthToken):
    """Handle Creating user authentication tokens"""
    # renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user": UserSerializer(user).data})


class DetailUserEndpoint(generics.RetrieveAPIView):
    # permission_classes = IsAuthenticated
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArtistListEndpoint(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class QuoteListEndpoint(generics.ListCreateAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['quote', 'song_title', 'artist__name', 'contributor__name','category__name', 'mood__name']

    def get_queryset(self):
        queryset = Quote.objects.all()
        mood_id = self.request.query_params.get("mood_id", None)
        genre_id = self.request.query_params.get("genre_id", None)
        artist_id = self.request.query_params.get("artist_id", None)

        if mood_id:
            mood = Mood.objects.get(pk=mood_id)
            queryset = Quote.objects.filter(mood=mood)
        elif genre_id:
            genre = Category.objects.get(pk=genre_id)
            queryset = Quote.objects.filter(category=genre)   
        elif artist_id:
            artist = Artist.objects.get(pk=artist_id)
            queryset = Quote.objects.filter(artist=artist) 
        return queryset


class CategoryListEndpoint(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MoodListEndpoint(generics.ListCreateAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
