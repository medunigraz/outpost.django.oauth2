from django.urls import re_path, path
from oauth2_provider.views import TokenView

from .views import (
    ApplicationCreateView,
    ApplicationDeleteView,
    ApplicationDetailView,
    ApplicationEditView,
    ApplicationListView,
    AuthorizationView,
)

app_name = "oauth2"

urlpatterns = [
    path("applications/", ApplicationListView.as_view(), name="list"),
    path("applications/<int:pk>/", ApplicationDetailView.as_view(), name="detail"),
    path("applications/new/", ApplicationCreateView.as_view(), name="create"),
    path("applications/<int:pk>/edit/", ApplicationEditView.as_view(), name="edit"),
    path(
        "applications/<int:pk>/delete/",
        ApplicationDeleteView.as_view(),
        name="delete",
    ),
    path("authorize/", AuthorizationView.as_view(), name="authorize"),
    path("token/", TokenView.as_view(), name="token"),
]
