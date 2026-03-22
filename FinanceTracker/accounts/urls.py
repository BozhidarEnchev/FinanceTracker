from django.urls import path

from FinanceTracker.accounts.views import AppUserListCreateAPIView, AppUserLoginAPIView, AppUserDetailAPIView

urlpatterns = [
    path('users/', AppUserListCreateAPIView.as_view(), name='users'),
    path('users/<int:pk>', AppUserDetailAPIView.as_view(), name='user_detail'),
    path('auth/login/', AppUserLoginAPIView.as_view(), name='login'),
]