from django.urls import path
from pages.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home_page_view.as_view(), name='home'),
    path('about/', About_page_view.as_view(), name='about'),
]
