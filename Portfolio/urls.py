from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, EduView, JobView, ContactView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('experience/', JobView.as_view(), name='about_job'),
    path('education/', EduView.as_view(), name='about_me'),
    path('', HomeView.as_view(), name='home')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)