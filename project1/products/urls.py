from django.urls import path
from .views import home_page,get_products

urlpatterns = [
    path('', home_page, name='home_page'),
    path('products/<int:pk>',get_products, name='get_products'),

]


