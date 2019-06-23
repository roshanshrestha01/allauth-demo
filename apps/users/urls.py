from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('sign-up/', views.SignUpTemplateView.as_view(), name='sign-up'),
    path('deactivate/', views.DeactivateView.as_view(), name='deactivate'),
    path('privacy-policy/', views.TemplateView.as_view(template_name='users/privacy-policy.html'), name='privacy-policy'),
]
