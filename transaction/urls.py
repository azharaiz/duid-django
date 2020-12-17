from django.urls import path
from .views import TransactionView, TransactionItemView

app_name = 'transaction'
urlpatterns = [
    path('', TransactionView.as_view()),
    path('<str:transaction_id>/', TransactionItemView.as_view())
]
