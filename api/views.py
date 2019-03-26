from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView
from .serializers import (ItemListSerializer, ItemDetailSerializer,UserCreateSerializer,
	CartCreateSerializer,CartListSerializer)
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from api.models import Item, Cart

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','description','price','category']

class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'

class CartListView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user',]

class CartCreateAPIView(CreateAPIView):
    serializer_class = CartCreateSerializer