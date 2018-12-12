import json
from django.test import TestCase
from ..models import Product,Famille,Laboratoire
from productAPI.serializers import ProductSerializer ,FamilleSerializer, LaboratoireSerializer
from rest_framework import status
from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework.test import APITestCase,APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User




class ProductsTests(APITestCase):

    @classmethod
    def setUpTestData(self):
        self.client = APIClient()
        Product.objects.create(
            designation = 'Produit 1',reference = '123abc',contenantCoffret=1,testContenant=1)
        Product.objects.create(
            designation = 'Produit 2',reference = '123def',contenantCoffret=2,testContenant=2)
        Famille.objects.create(designation ='Famille 1')
        Famille.objects.create(designation='Famille 2')
        Laboratoire.objects.create(designation = 'Laboratoire 1 ')
        Laboratoire.objects.create(designation = 'Laboratoire 2')
        user = User.objects.create_user('abdou', '', 'abdou')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(token.key))




    def test_product_creation(self):
        produit_1 = Product.objects.get(designation='Produit 1')
        produit_2 = Product.objects.get(designation='Produit 2')
        self.assertEqual(produit_1.designation,"Produit 1")
        self.assertEqual(produit_2.designation,"Produit 2")

    def test_get_all_products(self):

        #Retreive all products
        response = self.client.get('/products/')
        products = Product.objects.all()
        serializer = ProductSerializer(products , many=True)
        self.assertEqual(response.data , serializer.data,'Retreive many products')
        

    def test_post_product(self):

        produit_1 = Product(designation ='Produit_1',reference = '123abc',contenantCoffret=1,testContenant=1)
        famille_1 =  get_object_or_404(Famille ,id=1)
        laboratoire_1 = get_object_or_404(Laboratoire, id=1)
        produit_1.famille = famille_1
        produit_1.laboratoire = laboratoire_1

        serializer = ProductSerializer(produit_1)
        serializer.data['famille_id'] = famille_1.id
        serializer.data['laboratoire_id'] = laboratoire_1.id
        response = self.client.post(reverse('get_all_products'),serializer.data)
        self.assertEqual(response.data,serializer.data,'Post data');


    def test_get_product(self):

        #retreive one product
        response = self.client.get('/product/1/')
        product_1 = get_object_or_404(Product,pk=1)
        serializer = ProductSerializer(product_1)
        self.assertEqual(response.data , serializer.data,'Retreive one product')

        #edit product
        famille_1 =  get_object_or_404(Famille ,id=1)
        laboratoire_1 = get_object_or_404(Laboratoire, id=1)
        product_1.famille = famille_1
        product_1.laboratoire = laboratoire_1
        serializer = ProductSerializer(product_1)
        put_response = self.client.put('/product/1',serializer.data)
        get_response = self.client.get('/product/1/')
        self.assertEqual(get_response.data, serializer.data,'Edit one product')


