from rest_framework import serializers
from .models import Protein

class ProteinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ('id', 'name', 'searcheable', 'created_at')