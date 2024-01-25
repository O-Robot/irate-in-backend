from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AuthViewset, CustomObtainTokenPairView
from .google_auth.views import GoogleLoginAPIView, GoogleLoginRedirectAPIView


app_name = 'user'

router = DefaultRouter()
router.register('users', AuthViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomObtainTokenPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # path('google-auth/', GoogleLoginAPIView.as_view()),
    # path('google-auth/redirect/', GoogleLoginRedirectAPIView.as_view())
]
