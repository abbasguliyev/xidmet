from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model


def user_list() -> QuerySet:
    """
    Get all users.
    """
    return get_user_model().objects.all()