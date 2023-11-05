
from django.urls import path, include

from gallery.views import GalleryView


app_name = 'gallery'

urlpatterns = [
    path('', GalleryView.as_view(), name='index'),
]