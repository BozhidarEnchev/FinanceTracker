from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from FinanceTracker.accounts.models import AppUser
from FinanceTracker.accounts.serializers import RegisterSerializer, LoginSerializer, AppUserReadSerializer


class AppUserListCreateAPIView(ListCreateAPIView):
    serializer_class = RegisterSerializer
    queryset = AppUser.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAdminUser()]
        return [AllowAny()]


class AppUserDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AppUserReadSerializer
    def get_permissions(self):
        if self.request.user.pk == self.request.GET.get('pk'):
            return [IsAdminUser()]
        return [AllowAny()]

    def get_queryset(self):
        return AppUser.objects.filter(pk=self.request.user.id)

class AppUserLoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer
