from productAPI.models import Product, Famille, Laboratoire
from productAPI.serializers import ProductSerializer ,FamilleSerializer, LaboratoireSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response






@api_view(['GET', 'POST']) 
def product_search(request, designation):

    if request.method == 'GET':
        products = Product.objects.all().filter(designation=designation)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

def famille_search(request, designation):
    
    if request.method == 'GET':
        familles = Famille.objects.all().filter(designation=designation)
        serializer = FamilleSerializer(familles, many=True)
        return Response(serializer.data)

def laboratoire_search(request, designation):
    
    if request.method == 'GET':
        laboratoires = Laboratoire.objects.all().filter(designation=designation)
        serializer = LaboratoireSerializer(laboratoires, many=True)
        return Response(serializer.data)


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

class FamilleList(generics.ListCreateAPIView):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer


class FamilleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer

class LaboratoireList(generics.ListCreateAPIView):
    queryset = Laboratoire.objects.all()
    serializer_class = LaboratoireSerializer


class LaboratoireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laboratoire.objects.all()
    serializer_class = LaboratoireSerializer
