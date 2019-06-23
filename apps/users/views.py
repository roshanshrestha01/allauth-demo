from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class SignUpTemplateView(TemplateView):
    template_name = 'users/sign-up.html'


class DeactivateView(View):
    def post(self, request):
        user = request.user
        user.is_active = False
        # user.socialaccount_set.all().delete()
        user.save()
        logout(request)
        return redirect('sign-up')
