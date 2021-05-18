from rest_framework_simplejwt import views as jwt_views
from accounts import views
from django.urls import path, include

urlpatterns = [
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('register/', views.PersonsAPI.as_view(), name='register'),
]
