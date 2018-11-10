from rest_framework import serializers
from productAPI.models import Product, Famille, Laboratoire


class ProductSerializer(serializers.ModelSerializer):  

    
    class Meta:
        model = Product
        fields = '__all__'


class FamilleSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Famille
        fields = '__all__'

class LaboratoireSerializer(serializers.ModelSerializer):
     
    products = ProductSerializer(many=True, read_only=True)


    class Meta:
        model = Laboratoire
        fields = '__all__'

