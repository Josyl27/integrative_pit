from django.contrib import admin
from django.urls import path, include
from api.views import home,v1_ui,v2_ui
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Country Currency Integration API",
        default_version='v1',
        description="Integration of Country API and Currency Exchange API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    path("admin/", admin.site.urls),

    path("", include("api.urls")),

    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger-ui",
    ),

    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="redoc",
    ),
    path("",home),

    path("v1-ui/",v1_ui),

    path("v2-ui/",v2_ui),
]