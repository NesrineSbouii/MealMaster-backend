from django.urls import path, include
from .views import index

urlpatterns = [
   # path('', index, name='index'),
    path("", include("django.contrib.auth.urls")),
]
from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from .views import UserDetailAPI,RegisterUserAPIView


urlpatterns = [
   #path('login/', UserLogIn.as_view()),
  #  path('auth/', include('rest_framework.urls', namespace='rest_framework')),
  #  re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
#] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
]