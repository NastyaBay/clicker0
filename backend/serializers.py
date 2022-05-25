from rest_framework.serializers import ModelSerializer
from .models import Core, Boost

class CoreSerializer(ModelSerializer):
    class Meta:
        model = Core
        fields = ['coins', 'clikc_power']
        
class BoostSerializer(ModelSerializer):
    class Meta:
        model = Boost
        fields = '__all__'