from django.urls import path
from .views import getcategories,getcategoryproduct
urlpatterns =[
    path("getcategories",getcategories),
    path("getcategoryproduct",getcategoryproduct),
]