from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('sign-up/', views.SignUpTemplateView.as_view(), name='sign-up'),
    path('deactivate/', views.DeactivateView.as_view(), name='deactivate'),
]
