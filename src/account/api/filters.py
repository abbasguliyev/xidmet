from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model

class UserFilter(filters.FilterSet):
    """
    Filter class for User model.
    """
    class Meta:
        model = get_user_model()
        fields = {
            'email': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
        }
