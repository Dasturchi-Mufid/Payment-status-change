from rest_framework.serializers import ModelSerializer
from . import models

class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username')
        # depth = 1
        

class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'price')
        # depth = 1


class PaymentSerializer(ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer()
    
    class Meta:
        model = models.Payment
        fields = ('id', 'user','product','status', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
        
        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['status'] = instance.get_status_display()
            return representation

        