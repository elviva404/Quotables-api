from rest_framework import serializers
from quotables.models import User, Mood, Artist, Category, Quote
# from .fields import ReadableChoiceField

class UserSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': { 
                'write_only': True,
                'style': { 'input_type'}
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserProfile(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ArtistSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        request = self.context['request']
        artist = Artist.objects.create(**validated_data)
        return artist

    class Meta:
        model = Artist
        fields = (
            'id', 
            'name',
            'category',
            'profile_image_url',
            )


class MoodSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context['request']
        mood = Mood.objects.create(**validated_data)
        return mood

    class Meta:
        model = Mood
        fields = (
            'id', 
            'name', 
            'image_url',
            )


class CategorySerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        request = self.context['request']
        category = Category.objects.create(**validated_data)
        return category

    class Meta:
        model = Category
        fields = (
            'id', 
            'name', 
        )


class QuoteSerializer(serializers.ModelSerializer):

    artist = ArtistSerializer(read_only=True)
    contributor = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    mood = MoodSerializer(read_only=True)

    def create(self, validated_data):
        request = self.context['request']
        quote = Quote.objects.create(**validated_data)
        return quote

    class Meta:
        model = Quote
        fields = (
            'id', 
            'quote',
            'song_title', 
            'artist',
            'contributor', 
            'category', 
            'mood',
            'apple_music_url', 
            'spotify_url', 
            )