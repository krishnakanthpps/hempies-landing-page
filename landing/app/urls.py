from django.urls import path
from .views import startView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", startView, name="start"),
]

urlpatterns += staticfiles_urlpatterns()