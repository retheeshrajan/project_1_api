from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Item, Cart

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password','first_name','last_name','email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class ItemListSerializer(serializers.ModelSerializer):
    item_details = serializers.HyperlinkedIdentityField(
        view_name="api-detail",
        lookup_field="id",
        lookup_url_kwarg="item_id")
    class Meta:
        model = Item
        fields = ['name','description','price','image','item_details']

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemNameSerializer(serializers.ModelSerializer):
   class Meta:
        model = Item
        fields = ['name','image']


class CartListSerializer(serializers.ModelSerializer):
    item=ItemNameSerializer()
    class Meta:
        model = Item
        fields = ['item','quantity','price']

class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
