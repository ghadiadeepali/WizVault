from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mindlog.models import Card
from mindlog.serializers import CardSerializer
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

@api_view(["GET"])
def cardView(request):
    if request.method == "GET":
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)