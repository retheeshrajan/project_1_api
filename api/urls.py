from django.urls import path
from .views import UserCreateAPIView
from rest_framework_jwt.views import obtain_jwt_token
from api.views import (ItemListView,ItemDetailView,CartListView,CartCreateAPIView,UserUpdateView,CartUpdateView)

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('userupdate/<int:user_id>', UserUpdateView.as_view(), name='userupdate'),
    path('list/', ItemListView.as_view(), name='api-list'),
    path('details/<int:item_id>', ItemDetailView.as_view(), name='api-detail'),
    path('cart/', CartListView.as_view(), name='api-cart'),
    path('addcart/', CartCreateAPIView.as_view(), name='api-addcart'),
    path('updatecart/<int:card_id>', CartUpdateView.as_view(), name='api-updatecart'),
]