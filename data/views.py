from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from .models import Data
from .serializer import DataSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import permissions # In case you want to use IsAdmin permission

class DataList(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class DataDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Data.objects.all()
    serializer_class = DataSerializer

