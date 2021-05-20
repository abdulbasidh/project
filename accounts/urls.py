from rest_framework_simplejwt import views as jwt_views
from accounts import views
from django.urls import path, include
from .views import (
    FormRegisterApiView,
)

urlpatterns = [
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('register/', views.PersonsAPI.as_view(), name='register'),
    path('form/', views.FormRegisterApiView.as_view(), name='form'),
    path('login/', views.LoginApiView.as_view(), name='login'),
]
