from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .CategorySerializers import CategorySerializer
from authentication.models import User
import uuid

class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        category_list = Category.objects.filter(user=request.user)
        category_list_serialized = CategorySerializer(category_list, many = True)
        content = {
            'category_list' : category_list_serialized.data
        }
        return(Response(content))

class CategoryItemView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        category_id = request.data.get('category_id')
        try:
            category_item = Category.objects.get(category_id=category_id, user=request.user)
        except(ObjectDoesNotExist, ValidationError):
            raise NotFound(detail="data not found", code=404)

        category_item_serializer = CategorySerializer(category_item, many=False)

        return(Response(category_item_serializer.data))
        
    def delete(self, request):
        category_id = request.data.get('category_id')
        try:
            category_item = Category.objects.get(category_id=category_id, user=request.user)
        except(ObjectDoesNotExist, ValidationError):
            raise NotFound(detail="data not found", code=404)

        category_item.delete()
        content = {
                'message' : "success delete category"
        }
        return(Response(content))
