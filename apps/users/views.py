from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class SignUpTemplateView(TemplateView):
    template_name = 'users/sign-up.html'
