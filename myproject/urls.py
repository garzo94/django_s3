
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views
from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
# This handle the CRUD automatically
router.register('users', views.UserViewSet),


urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
