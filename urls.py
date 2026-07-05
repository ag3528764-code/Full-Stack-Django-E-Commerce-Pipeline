from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    path('payment/<int:product_id>/', views.process_payment, name='process_payment'),
]