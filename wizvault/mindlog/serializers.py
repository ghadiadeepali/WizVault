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
        fields = ['title', 'text_body', 'category','tags', 'source', 'image', 'is_favourite']
        extra_kwargs = {
            'tags': {'required': False},
            'source': {'required': False},
            'image': {'required': False},
            'is_favourite': {'required': False},
        }
        
        
class UpdateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['title', 'text_body', 'category','tags', 'source', 'image', 'is_favourite']
        extra_kwargs = {
            'title':{'required': False},
            'text_body':{'required': False},
            'category':{'required': False},
            'tags': {'required': False},
            'source': {'required': False},
            'image': {'required': False},
            'is_favourite': {'required': False},
        }
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class NewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']