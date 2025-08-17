from rest_framework import serializers
from .models import users, inventory, inventory_log, finances, finances_log, documents

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'

class inventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory
        fields = '__all__'

class inventory_logSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory_log
        fields = '__all__'

class financesSerializer(serializers.ModelSerializer):
    class Meta:
        model = finances
        fields = '__all__'

class finances_logSerializer(serializers.ModelSerializer):
    class Meta:
        model = finances_log
        fields = '__all__'

class documentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = documents
        fields = '__all__'