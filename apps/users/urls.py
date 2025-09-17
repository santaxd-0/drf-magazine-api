from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views
from django.urls import path

from .views import UserAPIView

user_router = SimpleRouter()
user_router.register(r"users", UserAPIView)

urlpatterns = [
    path("token/", views.TokenObtainPairView.as_view(), name="jwt-token-obtain"),
    path("token/refresh/", views.TokenRefreshView.as_view(), name="jwt-token-refresh")
]

urlpatterns += user_router.urls
