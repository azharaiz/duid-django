from django.urls import path, include
from rest_framework import routers

from target.views import TargetView

router = routers.DefaultRouter()
router.register('', TargetView, basename='target')

urlpatterns = [
    path('', include(router.urls)),

]
