from django.conf import settings
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Facebook App'

urlpatterns = [
    path('', include('apps.users.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),

                      # For django versions before 2.0:
                      # url(r'^__debug__/', include(debug_toolbar.urls)),

                  ] + urlpatterns
