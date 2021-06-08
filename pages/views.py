from django.views.generic import TemplateView

# Create your views here.


class Home_page_view(TemplateView):
    template_name = 'home.html'


class About_page_view(TemplateView):
    template_name = 'about.html'
