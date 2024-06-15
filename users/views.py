from django.contrib.auth import logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def logout_view(request):
    logout(request)


class PasswordResetCompleteView(PasswordResetView):
    template_name = 'registration/password_reset_complete.html'



