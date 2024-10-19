from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('register/', views.register, name='register'),  # URL for the register page
    path('toggle-dark-mode/', views.toggle_dark_mode, name='toggle_dark_mode'),
]
