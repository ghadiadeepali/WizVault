from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mindlog.models import Card, Category
from mindlog.serializers import CardSerializer, NewCardSerializer, CategorySerializer, NewCategorySerializer, UpdateCardSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Wizvault. Start storing wisdom here")



@api_view(["GET", "POST"])
def list_card_view(request):
    try:
        if request.method == "GET":
            cards = Card.objects.all()
            if cards:
                serializer = CardSerializer(cards, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message": "No Cards Found"}, status=status.HTTP_404_NOT_FOUND)
        
          
        if request.method == "POST":
            received_data = NewCardSerializer(data=request.data)
            if received_data.is_valid():
                saved_instance = received_data.save()  
                return Response(CardSerializer(saved_instance).data, status=status.HTTP_201_CREATED)
            
            return Response(received_data.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message": "Something went wrong", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def update_card_view(request, pk):
    try:
        card_to_update = Card.objects.get(pk=pk)
        if card_to_update:
            received_data = UpdateCardSerializer(card_to_update, data=request.data)
            if received_data.is_valid():
                saved_instance = received_data.save()
                return Response(CardSerializer(saved_instance).data,status=status.HTTP_200_OK)
            return Response({"message": received_data.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Card not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"message": "Something went wrong", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["DELETE"])
def delete_card_view(request, pk):
    try:
        card_to_delete = Card.objects.get(pk=pk)
        if card_to_delete:
            card_to_delete.delete()
            return Response({"message": "Card deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Card not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
         return Response({"message": "Something went wrong", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    
    

@api_view(["GET", "POST"])
def list_category_view(request):
    if request.method == "GET":
            categories = Category.objects.all()
            if categories:
                response_data = CategorySerializer(categories, many=True)
                return Response(response_data.data, status=status.HTTP_200_OK)
            return Response({"message": "No Categories Found"}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "POST":
        received_data = NewCategorySerializer(data=request.data)
        if received_data.is_valid():
            saved_instance = received_data.save()
            return Response(CategorySerializer(saved_instance).data, status=status.HTTP_200_OK)
        
        return Response(received_data.errors, status=status.HTTP_400_BAD_REQUEST)

            
@api_view(["PUT"])
def update_category_view(request, pk):
    try:
        category_to_update = Category.objects.get(pk=pk)
        if category_to_update:
            received_data = NewCategorySerializer(category_to_update, data=request.data)
            if received_data.is_valid():
                saved_instance = received_data.save()
                return Response(CategorySerializer(saved_instance).data,status=status.HTTP_200_OK )
            return Response({"message": received_data.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Category Not Found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"message": "Something went wrong", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["DELETE"])
def delete_category_view(request, pk):
    try:
        category_to_delete = Category.objects.get(pk=pk)
        if category_to_delete:
            category_to_delete.delete()
            return Response({"message": "Category Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Category Not Found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"message": "Something went wrong", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)