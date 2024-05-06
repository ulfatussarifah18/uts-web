
from rest_framework import viewsets
from .models import Anggota
from .serializers import AnggotaSerializer

class AnggotaViewSet(viewsets.ModelViewSet):
    queryset = Anggota.objects.all()
    serializer_class = AnggotaSerializer

 