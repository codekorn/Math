from django.urls import path
from pages.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', Home_page_view.as_view(), name='home'),
    path('about/', About_page_view.as_view(), name='about'),
]
urlpatterns += staticfiles_urlpatterns()
