"""
URL configuration for alfams project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = []

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')),]

    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]


urlpatterns += [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('gallery/', include('gallery.urls')),
    path('blog/', include('blog.urls')),
    path('shop/', include('product.urls')),
    path('cart/', include('ecommerce.urls')),
    #path('category/', include('product.urls'), name='main_category'),
    #path('product/', include('product.urls_ex'), name='main_product'),
    path('', include('website.urls')),
]