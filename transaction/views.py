from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction
from category.models import Category
from authentication.models import User
from dompet.models import Dompet
from .serializers import TransactionSerializer
from .util import UtilTransaction
import uuid
from django.shortcuts import get_object_or_404

class TransactionView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        account_id = request.query_params.get('account_id')
        category_id = request.query_params.get('category_id')
        transaction_list = UtilTransaction.conditional_transaction_filter(
            request.user, account_id, category_id
        )
        transaction_list_serialized = TransactionSerializer(transaction_list, many=True)
        content = {
            'transaction_list' : transaction_list_serialized.data
        }

        return Response(content)

    def post(self, request):
        transaction_data = TransactionSerializer(data=request.data)
        transaction_data.is_valid(raise_exception=True)
        dompet = get_object_or_404(
            Dompet, account_id=request.data.get("dompet")
        )
        category = get_object_or_404(
            Category, category_id=request.data.get("category")
        )
        Transaction.objects.create(
            dompet=dompet,
            category=category,
            user=request.user,
            amount=request.data.get("amount")
        )
        content = {
            'message' : "success add category"
        }
        return Response(content)
