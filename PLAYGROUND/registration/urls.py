from django.urls import path
from .views import SignUpView, ProfileUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),3.
    path('profile/', ProfileUpdate.as_view(), name='profile'),
]