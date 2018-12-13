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
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication





class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('designation','id')


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FamilleList(generics.ListCreateAPIView):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('designation',)

class FamilleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer

class LaboratoireList(generics.ListCreateAPIView):
    queryset = Laboratoire.objects.all()
    serializer_class = LaboratoireSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('designation',)

class LaboratoireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laboratoire.objects.all()
    serializer_class = LaboratoireSerializer


class TransactionList(generics.ListCreateAPIView):
    queryset = ProductTrans.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,)
    filter_fields =('trans_type',)
    search_fields =('product__designation',)


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductTrans.objects.all()
    serializer_class = TransactionSerializer


class StockList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('designation','id')


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    
    return Response({'user': user},status=status.HTTP_200_OK)