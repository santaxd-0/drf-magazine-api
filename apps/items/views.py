from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer, MagazineAPISerializer


class ItemAPI(viewsets.ModelViewSet):
    """
    Items list for an admins
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "slug"

class CategoryAPI(viewsets.ModelViewSet):
    """
    Categories list for an admins
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "id"

class MagazinePublicAPI(viewsets.ReadOnlyModelViewSet):
    """
    Public API for customers
    """
    queryset = Category.objects.all().order_by("id")
    serializer_class = MagazineAPISerializer
    # field for URI navigation
    lookup_field = "name"

    @action(detail=True, methods=["GET"], url_path="items")
    def get_items(self, request, name=None):
        category = self.get_object()
        # return a paginated QuerySet
        items = self.paginate_queryset(category.item_set.all().order_by("id"))
        serializer = ItemSerializer(items, many=True)
        # return a paginated response
        return self.get_paginated_response(serializer.data)

    @action(detail=True, methods=["GET"], url_path="items/(?P<item_slug>[-\w]+)")
    def get_item(self, request, name=None, item_slug=None):
        category = self.get_object()
        try:
            item = category.item_set.get(slug=item_slug)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=404) 
    