from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Authentication API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema_swagger_ui"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("authentication/", include("authentication.urls")),
]