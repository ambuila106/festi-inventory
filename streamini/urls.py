from django.contrib import admin
from django.urls import path, include
from social.urls import apiurls as social_apiurls
from medias.urls import apiurls as medias_apiurls

apiurls = ([
    path('social/', include(social_apiurls, namespace='social')),
    path('medias/', include(medias_apiurls, namespace='medias')),
], 'api')

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('admin/', admin.site.urls),
    path('api/', include(apiurls, namespace='api')),
]
