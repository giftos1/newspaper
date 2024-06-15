from django.contrib.auth.views import LoginView
from django.urls import path

from pages.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('accounts/login/', LoginView.as_view(), name='login'),
]