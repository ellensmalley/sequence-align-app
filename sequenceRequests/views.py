from .models import Protein
from .serializers import ProteinSerializer
from rest_framework import generics

class ProteinListCreate(generics.ListCreateAPIView):
    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer