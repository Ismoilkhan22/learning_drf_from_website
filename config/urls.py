from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path

schema_view = get_schema_view(
    openapi.Info(
        title="learning drf",
        default_version='v1',
        description="learning drf from web site ",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="your_email@domain.com"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  # Swagger uchun URL'larni qo'shish
                  path('admin/', admin.site.urls),
                  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                          name='schema-json'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  path("api/v1/", include('src.core.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
