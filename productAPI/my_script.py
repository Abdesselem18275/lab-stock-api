import json
from rest_framework.test import APITestCase,APIClient
from productAPI.models import Product,Famille,Laboratoire
from productAPI.serializers import ProductSerializer ,FamilleSerializer, LaboratoireSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework.test import APIRequestFactory






client = APIClient()
user = User.objects.get_by_natural_key('abdou')
token= Token.objects.get(user=user)
print("token = "+str(token))
client.credentials(HTTP_AUTHORIZATION='Token ' + str(token))
data = {}
data["username"] = "abdou"
data["password"] = "abdou"
response = client.post(reverse('login'),data)
print(response.data)


# product_1 = get_object_or_404(Product,pk=25)
# famille_1 =  get_object_or_404(Famille ,id=2)
# laboratoire_1 = get_object_or_404(Laboratoire, id=2)
# product_1.famille = famille_1
# product_1.laboratoire = laboratoire_1
# product_1.designation = 'Hello test'
# serializer = ProductSerializer(product_1)


