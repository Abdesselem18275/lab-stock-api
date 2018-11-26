from rest_framework import serializers
from productAPI.models import Product, Famille, Laboratoire,ProductTrans



class TransactionSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model = ProductTrans
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['produit'] = ProductSerializer(instance.produit).data
        return response

class ProductSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model = Product
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['famille'] = FamilleSerializer(instance.famille).data
        response['laboratoire'] = LaboratoireSerializer(instance.laboratoire).data
        return response


class FamilleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Famille
        fields = '__all__'
        
class LaboratoireSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Laboratoire
        fields = '__all__'

