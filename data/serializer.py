from rest_framework import serializers

from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'description', 'created_at','updated_at')
        model = Data