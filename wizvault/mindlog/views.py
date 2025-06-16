from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mindlog.models import Card
from mindlog.serializers import CardSerializer, NewCardSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Wizvault. Start storing wisdom here")

# def cardView(request):
#     cards = Card.objects.all()
#     # this returns object of type queryset
    
#     # Understanding the Queryset in detail
#     # Queryset is a collection of python objects. And to access attribute values we use object_instance.attribute
#     # for card in cards:
#     #     print("*"*10)
#     #     print("card: ",card) #Prints title of the card becuase in models we have defined __str__ to return card.title everytime we try to print that model
#     #     print("card title: ", card.title)
#     #     print("*************************")  
    
#     # serialising manually
#     cards_list = list(cards.values())
#     # values() automatically loops inside itself
#     # django creates this query SELECT id, title, category, body FROM card;
#     # Hence we get for all the instances and not only one
    
#     return JsonResponse(cards_list, safe=False)
#     # by default, JSON response assumes you are sending dictionary. If not then add safe=False to allow non-dict items. safe=false also enables django to determine the type like list, queryset, etc

@api_view(["GET", "POST"])
def cardView(request):
    if request.method == "GET":
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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
