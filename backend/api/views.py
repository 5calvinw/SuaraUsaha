from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import users, inventory, inventory_log, finances, finances_log, documents
from .serializers import userSerializer, inventorySerializer, inventory_logSerializer, financesSerializer, finances_logSerializer, documentsSerializer

class usersViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = userSerializer

class inventoryViewSet(viewsets.ModelViewSet):
    queryset = inventory.objects.all()
    serializer_class = inventorySerializer

class inventory_logViewSet(viewsets.ModelViewSet):
    queryset = inventory_log.objects.all()
    serializer_class = inventory_logSerializer

class financesViewSet(viewsets.ModelViewSet):
    queryset = finances.objects.all()
    serializer_class = financesSerializer

class finances_logViewSet(viewsets.ModelViewSet):
    queryset = finances_log.objects.all()
    serializer_class = finances_logSerializer

class documentsViewSet(viewsets.ModelViewSet):
    queryset = documents.objects.all()
    serializer_class = documentsSerializer
