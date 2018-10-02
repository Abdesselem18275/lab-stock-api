from rest_framework import serializers
from productAPI.models import Product, Famille, Laboratoire



class FamilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Famille
        fields = '__all__'

class LaboratoireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratoire
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):  
    familles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    laboratoires = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
