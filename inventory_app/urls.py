
from django.urls import path
from main_page import views

urlpatterns = [
    path('', views.inventory_page, name='inventory'),
    path('purchase/', views.purchase_page, name='purchase'),
    path('sales/', views.sales_page, name='sale'),
    path('make_purchase/', views.make_purchase, name='purchased'),
    path('make_sale/', views.make_sale, name="sold"),
]

