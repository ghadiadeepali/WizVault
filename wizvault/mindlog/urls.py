from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/v1/cards/", views.list_card_view),
    path("api/v1/card/<int:pk>", views.update_card_view, name="update_card"),
    path("api/v1/card/<int:pk>/delete", views.delete_card_view),
    path("api/v1/categories/", views.list_category_view),
    path("api/v1/category/<int:pk>/", views.update_category_view),
    path("api/v1/category/delete/<int:pk>/", views.delete_category_view),
    
    ]
  