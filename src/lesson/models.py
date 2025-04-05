from django.db import models
from django.contrib.auth import get_user_model

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lesson_images/')
    start_date = models.DateField()
    is_active = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

class LessonDate(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="dates")
    lesson_day = models.CharField(max_length=20)
    lesson_hour = models.TimeField()

class LessonVideo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="videos")
    video_url = models.URLField()
    video_title = models.CharField(max_length=200)

class UserLesson(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="lessons")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="users")
    is_active = models.BooleanField(default=False)
