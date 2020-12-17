from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.TargetView, basename='target')

urlpatterns = [
    path('', include(router.urls)),

]
