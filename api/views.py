from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Transaction
from .serializer import CategorySerializer, TransactionSerializer
# Create your views here.
class CategoryViewsets(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class TransactionViewsets(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer