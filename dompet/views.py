from django.shortcuts import render
from rest_framework import viewsets
from .models import Dompet
from .serializers import DompetSerializer


class DompetView(viewsets.ModelViewSet):
    queryset = Dompet.objects.all()
    serializer_class = DompetSerializer
