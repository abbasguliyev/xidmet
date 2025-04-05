from rest_framework import viewsets, status, permissions
from rest_framework.views import Response
from rest_framework.decorators import action
from account.api import selectors, serializers, services, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Custom Token Views with AllowAny permission
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = selectors.user_list()
    serializer_class = serializers.UserOutSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.UserFilter
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated],
        'retrieve': [permissions.IsAdminUser],
        'create': [permissions.AllowAny],
        'update': [permissions.IsAuthenticated],
        'partial_update': [permissions.IsAuthenticated],
        'destroy': [permissions.IsAdminUser],
    }

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.UserCreateSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return serializers.UserUpdateSerializer
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_user(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'detail': _("Əməliyyat yerinə yetirildi")}, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        services.update_user(instance=instance, **serializer.validated_data)
        return Response(data={'detail': _("Əməliyyat yerinə yetirildi")}, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False, serializer_class=serializers.UserOutSerializer, filterset_class=None, permission_classes=[permissions.IsAuthenticated], url_path="me")
    def me(self, request, *args, **kwargs):
        user = request.user
        user = selectors.user_list().filter(pk=user.pk).last()
        serializers = self.get_serializer(user)
        return Response(serializers.data)

    @action(methods=["POST"], detail=False, serializer_class=serializers.ChangePasswordSerializer, url_path="change-password", permission_classes=[permissions.IsAuthenticated])
    def change_password(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.change_password(instance=user, **serializer.validated_data)
        return Response(data={'detail': _("Şifrə yeniləndi")}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)