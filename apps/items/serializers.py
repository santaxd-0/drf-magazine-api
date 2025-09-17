from rest_framework import serializers
from django.utils.text import slugify

from .models import Item, Category


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "slug", "price", "discount", "category"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class MagazineAPISerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    def get_slug(self, obj):
        return slugify(obj.name)

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "item_set"]
        depth = 1

# class MagazineAPISerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = ["id", "name", "item_set"]