from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import APILogoutView

urlpatterns = [
    path('authenticate/', TokenObtainPairView.as_view(), name='authenticate'),
    path('authenticate/refresh/', TokenRefreshView.as_view(), name='authenticate_refresh'),
    path('logout/', APILogoutView.as_view(), name='logout'),
]