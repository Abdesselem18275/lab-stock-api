from productAPI.models import Product, Famille, Laboratoire
from productAPI.serializers import ProductSerializer ,FamilleSerializer, LaboratoireSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST']) 
def product_search(request, designation):
    if request.method == 'GET':
        products = Product.objects.all().filter(designation__icontains=designation)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST']) 
def famille_search(request, designation):
    if request.method == 'GET':
        familles = Famille.objects.all().filter(designation__icontains=designation)
        serializer = FamilleSerializer(familles, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST']) 
def laboratoire_search(request, designation):
    if request.method == 'GET':
        laboratoires = Laboratoire.objects.all().filter(designation__icontains=designation)
        serializer = LaboratoireSerializer(laboratoires, many=True)
        return Response(serializer.data)


class ProductList(APIView):
    def get(self,format='json'):
        products = Product.objects.all();
        serializer = ProductSerializer(products , many = True)
        return Response(serializer.data)
    def post(self,format='json'):
        serializer = ProductSerializer(data=self.request.data)
        if not(serializer.is_valid(raise_exception=ValueError)):
            return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

        serializer.create(validated_data=self.request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductDetail(APIView):

    def get(self ,request, pk):
        product = get_object_or_404(Product,pk=pk)
        return Response(ProductSerializer(product).data)

    # def put(self,request,pk,format='json'):
        
        
    #     instance=get_object_or_404(Product,pk=pk)
    #     ProductSerializer(data=request.data)
    #     serializer = ProductSerializer(data=request.data)
    #     if not(serializer.is_valid(raise_exception=ValueError)):
    #        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

    #     updated_inst=serializer.update(instance,validated_data=request.data)
    #     return Response(ProductSerializer(updated_inst).data, status=status.HTTP_201_CREATED)





@method_decorator(csrf_exempt, name='dispatch')
class FamilleList(generics.ListCreateAPIView):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer

@method_decorator(csrf_exempt, name='dispatch')
class FamilleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer

@method_decorator(csrf_exempt, name='dispatch')
class LaboratoireList(generics.ListCreateAPIView):
    queryset = Laboratoire.objects.all()
    serializer_class = LaboratoireSerializer

@method_decorator(csrf_exempt, name='dispatch')
class LaboratoireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laboratoire.objects.all()
    serializer_class = LaboratoireSerializer
