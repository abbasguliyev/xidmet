from django_filters import rest_framework as filters
from lesson.models import Lesson, LessonDate, LessonVideo, UserLesson

class LessonFilter(filters.FilterSet):
    class Meta:
        model = Lesson
        fields = {
            'name': ['exact', 'icontains'],
            'start_date': ['exact', 'gte', 'lte'],
            'is_active': ['exact'],
            'is_completed': ['exact'],
        }

class LessonDateFilter(filters.FilterSet):
    class Meta:
        model = LessonDate
        fields = {
            'lesson__name': ['exact', 'icontains'],
            'lesson_day': ['exact'],
            'lesson_hour': ['exact', 'gte', 'lte'],
        }

class LessonVideoFilter(filters.FilterSet):
    class Meta:
        model = LessonVideo
        fields = {
            'lesson__name': ['exact', 'icontains'],
            'video_title': ['exact', 'icontains'],
        }

class UserLessonFilter(filters.FilterSet):
    class Meta:
        model = UserLesson
        fields = {
            'lesson__name': ['exact', 'icontains'],
            'is_active': ['exact'],
        }
