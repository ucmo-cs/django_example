from django.urls import path
from cars import views

urlpatterns = [
    path('cars', views.cars_list),
    path('cars/<int:pk>', views.cars_detail),
    path('cars/make/<slug:tm>', views.cars_model_list),
]
