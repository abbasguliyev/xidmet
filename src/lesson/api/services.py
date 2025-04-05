from lesson.models import Lesson, LessonDate, LessonVideo, UserLesson

def create_lesson(*, name: str, image: str, start_date: str, is_active: bool, is_completed: bool) -> Lesson:
    """
    Create a new lesson.
    """
    lesson = Lesson.objects.create(
        name=name,
        image=image,
        start_date=start_date,
        is_active=is_active,
        is_completed=is_completed
    )

    return lesson

def update_lesson(instance: Lesson, **kwargs) -> Lesson:
    """
    Update an existing lesson.
    """
    for attr, value in kwargs.items():
        setattr(instance, attr, value)
    instance.save()

    return instance

def delete_lesson(instance: Lesson) -> None:
    """
    Delete a lesson.
    """
    instance.delete()

def create_lesson_date(*, lesson: Lesson, lesson_day: str, lesson_hour: str) -> LessonDate:
    """
    Create a new lesson date.
    """
    lesson_date = LessonDate.objects.create(
        lesson=lesson,
        lesson_day=lesson_day,
        lesson_hour=lesson_hour
    )

    return lesson_date

def update_lesson_date(instance: LessonDate, **kwargs) -> LessonDate:
    """
    Update an existing lesson date.
    """
    for attr, value in kwargs.items():
        setattr(instance, attr, value)
    instance.save()

    return instance

def delete_lesson_date(instance: LessonDate) -> None:
    """
    Delete a lesson date.
    """
    instance.delete()

def create_lesson_video(*, lesson: Lesson, video_url: str, video_title: str) -> LessonVideo:
    """
    Create a new lesson video.
    """
    lesson_video = LessonVideo.objects.create(
        lesson=lesson,
        video_url=video_url,
        video_title=video_title
    )

    return lesson_video

def update_lesson_video(instance: LessonVideo, **kwargs) -> LessonVideo:
    """
    Update an existing lesson video.
    """
    for attr, value in kwargs.items():
        setattr(instance, attr, value)
    instance.save()

    return instance

def delete_lesson_video(instance: LessonVideo) -> None:
    """
    Delete a lesson video.
    """
    instance.delete()

def create_user_lesson(*, user, lesson: Lesson, is_active: bool) -> UserLesson:
    """
    Create a new user lesson.
    """
    user_lesson = UserLesson.objects.create(
        user=user,
        lesson=lesson,
        is_active=is_active
    )

    return user_lesson

def update_user_lesson(instance: UserLesson, **kwargs) -> UserLesson:
    """
    Update an existing user lesson.
    """
    for attr, value in kwargs.items():
        setattr(instance, attr, value)
    instance.save()

    return instance

def delete_user_lesson(instance: UserLesson) -> None:
    """
    Delete a user lesson.
    """
    instance.delete()