from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnggotaViewSet

router = DefaultRouter()
router.register(r'anggota', AnggotaViewSet)

urlpatterns = [
    path('anggota/', include(router.urls)),
]

