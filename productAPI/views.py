from productAPI.models import Product, Famille, Laboratoire
from productAPI.serializers import ProductSerializer ,FamilleSerializer, LaboratoireSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator







@api_view(['GET', 'POST']) 
def product_search(request, designation):

    if request.method == 'GET':
        products = Product.objects.all().filter(designation=designation)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST']) 
def famille_search(request, designation):
    
    if request.method == 'GET':
        familles = Famille.objects.all().filter(designation=designation)
        serializer = FamilleSerializer(familles, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST']) 
def laboratoire_search(request, designation):
    
    if request.method == 'GET':
        laboratoires = Laboratoire.objects.all().filter(designation=designation)
        serializer = LaboratoireSerializer(laboratoires, many=True)
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

@method_decorator(csrf_exempt, name='dispatch')    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

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
