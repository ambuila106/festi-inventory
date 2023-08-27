from django.contrib import admin
from django.urls import path, include, re_path
from social.urls import apiurls as social_apiurls
from medias.urls import apiurls as medias_apiurls

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API del proyecto Streamini",
        default_version='v1',
        description="Descripción del API",
        contact=openapi.Contact(email="admin@streamini.com"),
        license=openapi.License(name="Streamini Rigths"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

apiurls = ([
    path('social/', include(social_apiurls, namespace='social')),
    path('medias/', include(medias_apiurls, namespace='medias')),
], 'api')

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('admin/', admin.site.urls),
    path('api/', include(apiurls, namespace='api')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
