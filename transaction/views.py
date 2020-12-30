from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from category.models import Category
from dompet.models import Dompet

from .models import Transaction
from .serializers import TransactionSerializer
from .util import UtilTransaction


class TransactionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        account_id = request.query_params.get('account_id')
        category_id = request.query_params.get('category_id')
        transaction_list = UtilTransaction.conditional_transaction_filter(
            request.user, account_id, category_id
        )
        transaction_list_serialized = TransactionSerializer(
            transaction_list, many=True)
        content = {
            'transaction_list': transaction_list_serialized.data
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
            'message': "success add category"
        }
        return Response(content)


class TransactionItemView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, transaction_id):
        transaction_item = get_object_or_404(
            Transaction, transaction_id=transaction_id
        )
        transaction_item.delete()
        content = {
            'message': "success delete transaction"
        }
        return Response(content)

    def put(self, request, transaction_id):
        transaction_item = get_object_or_404(
            Transaction, transaction_id=transaction_id
        )
        transaction_data = TransactionSerializer(
            instance=transaction_item, data=request.data
        )
        transaction_data.is_valid(raise_exception=True)
        transaction_data.save()
        content = {
            'message': "success add transaction"
        }
        return Response(content)
