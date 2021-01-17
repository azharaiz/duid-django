from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/dompet/', include('dompet.urls'), name='dompet_base'),
    path('api/auth/', include(('authentication.urls', 'authentication'), namespace='duid_auth')),
    path('api/category/', include('category.urls', namespace='category')),
    path('api/user/', include(('user.urls', 'user'), namespace='duid_user'))
    path('api/target/', include('target.urls')),
    path('api/transaction/', include('transaction.urls', namespace='transaction'))
]
