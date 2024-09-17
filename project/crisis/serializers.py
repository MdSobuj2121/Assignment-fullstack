from rest_framework import serializers
from .models import Crisis

class CrisisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crisis
        fields = '__all__'
