
from django.urls import path

from website.views import HomeView, HomeRedirectView, PagesView, SubPagesView


app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', HomeRedirectView.as_view(), name='home_redirect'),
    path('<slug:page_slug>/', PagesView.as_view() , name='pages'),
    path('<slug:page_slug>/<slug:page_slug_1>/', SubPagesView.as_view(), name='pages_1'),
]