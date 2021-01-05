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
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class CategoryListEndpoint(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MoodListEndpoint(generics.ListCreateAPIView):
    queryset = Mood.objects.all()
    serializer_class = CategorySerializer