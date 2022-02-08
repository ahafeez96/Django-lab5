from rest_framework import serializers
from pages.models import Track
class Trackserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Track
        fields=['name']