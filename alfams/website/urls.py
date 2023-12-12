
from django.urls import path
from django.views.decorators.cache import cache_page

from website.views import HomeView, HomeRedirectView, PagesView, SubPagesView


app_name = 'pages'
cache_time = 60*60*24

urlpatterns = [
    path('', cache_page(cache_time)(HomeView.as_view()), name='home'),
    path('home/', HomeRedirectView.as_view(), name='home_redirect'),
    path('<slug:page_slug>/', cache_page(cache_time)(PagesView.as_view()), name='pages'),
    path('<slug:page_slug_1>/<slug:page_slug>/', cache_page(cache_time)(SubPagesView.as_view()), name='pages_1'),
]