from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock, name='stock'),
    path('<slug:category_slug>/', views.stock, name='products_in_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_info, name='product_info'),
] 
