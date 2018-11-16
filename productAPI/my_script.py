import json
from rest_framework.test import APITestCase,APIClient
from productAPI.models import Product,Famille,Laboratoire
from productAPI.serializers import ProductSerializer ,FamilleSerializer, LaboratoireSerializer
from django.shortcuts import get_object_or_404

client = APIClient()
product_1 = get_object_or_404(Product,pk=25)
famille_1 =  get_object_or_404(Famille ,id=2)
laboratoire_1 = get_object_or_404(Laboratoire, id=2)
product_1.famille = famille_1
product_1.laboratoire = laboratoire_1
product_1.designation = 'Hello test'
serializer = ProductSerializer(product_1)
put_response = client.put('/product/25/',serializer.data,format='json')


