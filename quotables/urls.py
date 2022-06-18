from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quotables import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('users', views.UserEndpoint.as_view()),
    path('users/<int:pk>', views.DetailUserEndpoint.as_view()),
    path('login', obtain_auth_token),
    path('moods', views.MoodListEndpoint.as_view()),
    path('categories', views.CategoryListEndpoint.as_view()),
    path('quotes', views.QuoteListEndpoint.as_view()),
    path('artists', views.ArtistListEndpoint.as_view()),
]