from rest_framework import serializers
from musicstore.models import MusicWork, MusicWorkFile

#  The Serializer for MusicWork API definition.
class MusicWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicWork
        fields = '__all__'

#  The Serializer for MusicWorkFile API definition.
class MusicWorkFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicWorkFile
        fields = '__all__'
