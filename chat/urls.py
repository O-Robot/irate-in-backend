from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'chat'

router = DefaultRouter()
router.register('user-chats', views.ChatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.index, name='index'),
    path('home/<str:room_name>/', views.room, name='room'),
]
