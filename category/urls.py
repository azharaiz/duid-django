from django.urls import path
from .views import CategoryView, CategoryItemView

app_name = 'category'
urlpatterns = [
    path('', CategoryView.as_view()),
    path('<str:category_id>/', CategoryItemView.as_view())
]
