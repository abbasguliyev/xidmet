from django.urls import path, include

urlpatterns = [
    path('auth/', include('account.api.urls')),
    path('lessons/', include('lesson.api.urls')),
]