from rest_framework import serializers
from mindlog.models import Card, Category

# for displaying all the fields
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields = "__all__"
        
        
class NewCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'title', 'text_body', 'category', 'created_at', 'updated_at']
        # all 6 fields will be shown in output but the below 3 will be ignored in input
        read_only_fields = ['id', 'created_at', 'updated_at']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class NewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']