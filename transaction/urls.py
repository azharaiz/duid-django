from django.urls import path
from .views import TransactionView

app_name = 'transaction'
urlpatterns = [
    path('', TransactionView.as_view()),
]
