from rest_framework import serializers
from lesson.models import Lesson, LessonDate, LessonVideo, UserLesson

class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'image', 'start_date', 'is_active', 'is_completed']

class LessonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'image', 'start_date', 'is_active', 'is_completed']
        extra_kwargs = {
            'name': {'required': False},
            'image': {'required': False},
            'start_date': {'required': False},
            'is_active': {'required': False},
            'is_completed': {'required': False}
        }

class LessonOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'image', 'start_date', 'is_active', 'is_completed']
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
            'image': {'read_only': True},
            'start_date': {'read_only': True},
            'is_active': {'read_only': True},
            'is_completed': {'read_only': True}
        }

class LessonDateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDate
        fields = ['lesson', 'lesson_day', 'lesson_hour']

class LessonDateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDate
        fields = ['lesson', 'lesson_day', 'lesson_hour']
        extra_kwargs = {
            'lesson': {'required': False},
            'lesson_day': {'required': False},
            'lesson_hour': {'required': False}
        }

class LessonDateOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDate
        fields = ['id', 'lesson', 'lesson_day', 'lesson_hour']
        extra_kwargs = {
            'id': {'read_only': True},
            'lesson': {'read_only': True},
            'lesson_day': {'read_only': True},
            'lesson_hour': {'read_only': True}
        }

class LessonVideoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonVideo
        fields = ['lesson', 'video_url', 'video_title']

class LessonVideoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonVideo
        fields = ['lesson', 'video_url', 'video_title']
        extra_kwargs = {
            'lesson': {'required': False},
            'video_url': {'required': False},
            'video_title': {'required': False}
        }
class LessonVideoOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonVideo
        fields = ['id', 'lesson', 'video_url', 'video_title']
        extra_kwargs = {
            'id': {'read_only': True},
            'lesson': {'read_only': True},
            'video_url': {'read_only': True},
            'video_title': {'read_only': True}
        }

class UserLessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLesson
        fields = ['user', 'lesson', 'is_active']
        extra_kwargs = {
            'is_active': {'required': False}
        }

class UserLessonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLesson
        fields = ['user', 'lesson', 'is_active']
        extra_kwargs = {
            'user': {'required': False},
            'lesson': {'required': False},
            'is_active': {'required': False}
        }
class UserLessonOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLesson
        fields = ['id', 'user', 'lesson', 'is_active']
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
            'lesson': {'read_only': True},
            'is_active': {'read_only': True}
        }