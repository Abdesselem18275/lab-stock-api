from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.urls import reverse



# Using the standard RequestFactory API to create a form POST request

user = User.objects.get(username='root')

url = reverse('login')
print(user)

client = APIClient()

client.force_authenticate(user=user)
request = client.post('http://localhost:8000/login/', {'username': 'root','password': 'root'},format='json')
print(request)
