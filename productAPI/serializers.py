from rest_framework import serializers
from productAPI.models import Product, Famille, Laboratoire


class ProductSerializer(serializers.ModelSerializer):  

    
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class FamilleSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Famille
        fields = '__all__'

class LaboratoireSerializer(serializers.ModelSerializer):
     

    class Meta:
        model = Laboratoire
        fields = '__all__'

