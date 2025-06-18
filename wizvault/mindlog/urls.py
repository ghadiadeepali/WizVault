from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/v1/cards/", views.cardView),
    path("api/v1/card/<int:pk>", views.updateCardView, name="update_card"),
    path("api/v1/card/<int:pk>/delete", views.deleteCardView)
    
    ]
  