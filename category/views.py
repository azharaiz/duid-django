from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .CategorySerializers import CategorySerializer

class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        category_list = Category.objects.filter(user=request.user)
        category_list_serialized = CategorySerializer(category_list, many = True)
        content = {
            'category_list' : category_list_serialized.data
        }
        return(Response(content))

