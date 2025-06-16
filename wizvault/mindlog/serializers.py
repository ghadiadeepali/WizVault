from rest_framework import serializers
from mindlog.models import Card, Category

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields = "__all__"