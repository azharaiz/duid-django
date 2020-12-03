from django.urls import path
from .views import CategoryListView, CategoryItemView

app_name = 'category'
urlpatterns = [
    path('all/', CategoryListView.as_view()),
    path('item/', CategoryItemView.as_view())
]
