from django.db.models.query import QuerySet
from lesson.models import Lesson, LessonDate, LessonVideo, UserLesson


def lesson_list() -> QuerySet[Lesson]:
    """
    Get all lessons.
    """
    return Lesson.objects.all()

def lesson_date_list() -> QuerySet[LessonDate]:
    """
    Get all lesson dates
    """
    return LessonDate.objects.select_related("lesson").all()

def lesson_video_list() -> QuerySet[LessonVideo]:
    """
    Get all lesson videos
    """
    return LessonVideo.objects.select_related("lesson").all()

def user_lesson_list() -> QuerySet[UserLesson]:
    """
    Get all user lessons
    """
    return UserLesson.objects.select_related("user", "lesson").all()