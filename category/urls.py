from django.urls import path
from .views import CategoryListView

app_name = 'category'
urlpatterns = [
    path('all/', CategoryListView.as_view()),
]
