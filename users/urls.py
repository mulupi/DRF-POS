from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('createattendant/', views.add_attendant, name="adding_shop_attendant"),
    path('createmanager/', views.add_manager, name="adding_shop_manager"),
    path('get_user/', views.getUser, name="return_user"),
    path('get_all_user/', views.getUsers, name="return_users"),
]