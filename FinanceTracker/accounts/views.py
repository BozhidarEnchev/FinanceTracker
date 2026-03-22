from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AppUser.objects.filter(pk=self.request.user.pk)


class AppUserLoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer
