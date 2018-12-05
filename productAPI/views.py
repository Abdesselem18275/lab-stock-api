from productAPI.models import Product, Famille, Laboratoire,ProductTrans
from productAPI.serializers import TransactionSerializer,ProductSerializer ,FamilleSerializer, LaboratoireSerializer
from rest_framework import generics,status,filters
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend




@method_decorator(csrf_exempt, name='dispatch')
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('designation','id')


@method_decorator(csrf_exempt, name='dispatch')
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@method_decorator(csrf_exempt, name='dispatch')
class FamilleList(generics.ListCreateAPIView):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('designation',)

@method_decorator(csrf_exempt, name='dispatch')
class FamilleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer

@method_decorator(csrf_exempt, name='dispatch')
class LaboratoireList(generics.ListCreateAPIView):
    queryset = Laboratoire.objects.all()
    serializer_class = LaboratoireSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('designation',)

@method_decorator(csrf_exempt, name='dispatch')
class LaboratoireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laboratoire.objects.all()
    serializer_class = LaboratoireSerializer


@method_decorator(csrf_exempt, name='dispatch')
class TransactionList(generics.ListCreateAPIView):
    queryset = ProductTrans.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,)
    filter_fields =('trans_type',)
    search_fields =('product__designation',)


@method_decorator(csrf_exempt, name='dispatch')
class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductTrans.objects.all()
    serializer_class = TransactionSerializer


@method_decorator(csrf_exempt, name='dispatch')
class StockList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('designation','id')


@method_decorator(csrf_exempt, name='dispatch')
class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
