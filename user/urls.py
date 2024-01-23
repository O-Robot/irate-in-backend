from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewset


app_name = 'user'

router = DefaultRouter()
router.register('users', AuthViewset)

urlpatterns = [
    path('', include(router.urls)),
]
