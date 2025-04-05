from rest_framework import viewsets, permissions, status
from rest_framework.views import Response
from rest_framework.decorators import action
from lesson.api import selectors, filters, services, serializers
from django_filters.rest_framework import DjangoFilterBackend

class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lessons to be viewed or edited.
    """
    queryset = selectors.lesson_list()
    serializer_class = serializers.LessonOutSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.LessonFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.LessonCreateSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return serializers.LessonUpdateSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_lesson(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'detail': _("Əməliyyat yerinə yetirildi")}, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        services.update_lesson(instance=instance, **serializer.validated_data)
        return Response(data={'detail': _("Əməliyyat yerinə yetirildi")}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LessonDateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lesson dates to be viewed or edited.
    """
    queryset = selectors.lesson_date_list()
    serializer_class = serializers.LessonDateOutSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.LessonDateFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.LessonDateCreateSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return serializers.LessonDateUpdateSerializer
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_lesson_date(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'detail': _("Əməliyyat yerinə yetirildi")}, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        services.update_lesson_date(instance=instance, **serializer.validated_data)
        return Response(data={'detail': _("Əməliyyat yerinə yetirildi")}, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LessonVideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lesson videos to be viewed or edited.
    """
    queryset = selectors.lesson_video_list()
    serializer_class = serializers.LessonVideoOutSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.LessonVideoFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.LessonVideoCreateSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return serializers.LessonVideoUpdateSerializer
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_lesson_video(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'detail': _("Əməliyyat yerinə yetirildi")}, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        services.update_lesson_video(instance=instance, **serializer.validated_data)
        return Response(data={'detail': _("Əməliyyat yerinə yetirildi")}, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserLessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user lessons to be viewed or edited.
    """
    queryset = selectors.user_lesson_list()
    serializer_class = serializers.UserLessonOutSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.UserLessonFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.UserLessonCreateSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return serializers.UserLessonUpdateSerializer
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.create_user_lesson(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'detail': _("Əməliyyat yerinə yetirildi")}, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        services.update_user_lesson(instance=instance, **serializer.validated_data)
        return Response(data={'detail': _("Əməliyyat yerinə yetirildi")}, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)