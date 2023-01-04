from django.urls import path, include
from . import views as test_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', test_views.base_html, name='base_html'),
]