from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_photo, name='upload'),
    path('photo/<int:pk>/', views.photo_detail, name='detail'),
]
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls')),
]
