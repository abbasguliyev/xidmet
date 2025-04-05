from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LessonViewSet, LessonDateViewSet, LessonVideoViewSet, UserLessonViewSet

router = DefaultRouter()
router.register(r'lesson-date', LessonDateViewSet, basename='lesson-date')
router.register(r'lesson-video', LessonVideoViewSet, basename='lesson-video')
router.register(r'user-lesson', UserLessonViewSet, basename='user-lesson')
router.register(r'', LessonViewSet, basename='lesson')

urlpatterns = [
    path('', include(router.urls)),
]