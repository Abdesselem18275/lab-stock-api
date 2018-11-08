from rest_framework.test import APIClient

client = APIClient()

famille = {'designation': 'Familly client test'}
#client.put('/famille/1',famille, format='json')
client.get('/products')
