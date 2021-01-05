from rest_framework import serializers
from api.models import UserProfile, Car, Booking
from .fields import ReadableChoiceField

class UserSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile
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
