from django.urls import path
from pages.views import *

urlpatterns = [
    path('', Home_page_view.as_view(), name='home'),
    path('about/', About_page_view.as_view(), name='about'),
]
