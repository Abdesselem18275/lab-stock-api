from rest_framework import serializers
from productAPI.models import Product, Famille, Laboratoire



class FamilleSerializer(serializers.ModelSerializer):

    products = serializers.StringRelatedField(many=True)
    class Meta:
        model = Famille
        fields = '__all__'

class LaboratoireSerializer(serializers.ModelSerializer):
     
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Laboratoire
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):  
    

    class Meta:
        model = Product
        fields = '__all__'
