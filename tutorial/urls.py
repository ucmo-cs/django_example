from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('cars.urls')),
    path('', TemplateView.as_view(template_name="index.html")),
    path('index', TemplateView.as_view(template_name="index.html")),
]

