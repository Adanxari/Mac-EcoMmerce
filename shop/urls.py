from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about',views.about,name='AboutUs'),
    path('contacts',views.contacts,name='contacts'),
    path('tracker',views.tracker,name='trackStatus'),
    path('search',views.search,name='search'),
    path('productView/<int:myid>',views.productView,name='productView'),
    path('checkout',views.checkout,name='checkout')
]