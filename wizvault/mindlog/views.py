from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mindlog.models import Card, Category
from mindlog.serializers import CardSerializer, NewCardSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Wizvault. Start storing wisdom here")



@api_view(["GET", "POST"])
def list_card_view(request):
    if request.method == "GET":
        cards = Card.objects.all()
        # cards variable contains a list of Card objects (called queryset )where each element represents a row from the Card Table 
        serializer = CardSerializer(cards, many=True)
        # need to convert the queryset into python dictionary
        return Response(serializer.data, status=status.HTTP_200_OK)
        # serializer.data gives the structured data but it is not JSON (Still in Python land but not JSOn)
    
    # if request.method == "POST":
    #     serializer = NewCardSerializer(data=request.data)
    #     if serializer.is_valid():
    #         new_card = serializer.save()
            
    #         output_format = CardSerializer(new_card)
    #         # This validates based on field types, required fields, model constraints, etc.
    #         # once save is called, serializer variable now holds the saved object
    #         # on doing serializer.data it switches to serialization mode internally
    #         return Response(output_format.data, status=status.HTTP_201_CREATED)
        
    #     print("❌ Validation failed:", serializer.errors)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "POST":
        serializer = NewCardSerializer(data=request.data)  # Same serializer
        if serializer.is_valid():
            serializer.save()  # Everything works smoothly
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_card_view(request, pk):
    try:
        card = Card.objects.get(pk=pk)
    except Card.DoesNotExist:
        return Response({"error": "Card not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = NewCardSerializer(card, data=request.data)  # Or CardSerializer if you want full fields
    if serializer.is_valid():
        updated_card = serializer.save()
        card_info = CardSerializer(updated_card)
        return Response(card_info.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_card_view(request, pk):
    try:
        card = Card.objects.get(pk=pk)
    except Card.DoesNotExist:
        return Response({"error": "Card not found."}, status=status.HTTP_404_NOT_FOUND)
    
    card.delete()
    return Response({"message": "Card deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def list_category_view(request):
    if request.method == "GET":
        try:
            categories = Category.objects.all()
            
            if categories.exists():
                serializer = CategorySerializer(categories, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message": "No categories found."}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({"error": f"Something went wrong: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                
    
        