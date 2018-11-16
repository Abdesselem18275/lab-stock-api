from rest_framework import serializers
from productAPI.models import Product, Famille, Laboratoire


class ProductSerializer(serializers.ModelSerializer):  
    
    
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

    def create(self ,validated_data) :

       try: 
        famille_data = validated_data.pop('famille') 
        laboratoire_data = validated_data.pop('laboratoire') 
        famille = Famille(id=famille_data.pop('id'),designation=famille_data.pop('designation'))
        laboratoire = Laboratoire(id=laboratoire_data.pop('id'),designation=laboratoire_data.pop('designation'))
       except AttributeError:
        famille = Famille()
        laboratoire = Laboratoire()

       product = Product.objects.create(**validated_data,famille=famille,laboratoire=laboratoire)
       return product;

    def update(self ,instance,validated_data) :
        ##### warnning!!!!! Pop remove the selected element !!! 
       print('validated_data   '+str(validated_data))
       famille_data = validated_data.pop('famille');
       laboratoire_data = validated_data.get('laboratoire');
       instance.famille = Famille(id=famille_data.pop('id'),designation=famille_data.pop('designation'))
       instance.laboratoire = Laboratoire(id=laboratoire_data.pop('id'),designation=laboratoire_data.pop('designation'))
       instance.save()
       return instance



class FamilleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Famille
        fields = '__all__'
        

class LaboratoireSerializer(serializers.ModelSerializer):
     

    class Meta:
        model = Laboratoire
        fields = '__all__'

