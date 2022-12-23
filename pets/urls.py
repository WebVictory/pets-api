from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from pets import views

router = routers.DefaultRouter()
router.register(r'pets', views.PetsViewSet, basename='pets')
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)