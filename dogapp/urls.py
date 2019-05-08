from django.urls import path
from .views import list_dogs, create_dog, update_dog, list_customers, create_customer, update_customer, delete_dog, delete_customer

urlpatterns = [
    path('', list_dogs, name='list_dogs'),
    path('new', create_dog, name='create_dog'),
    path('update/<int:id>/', update_dog, name='update_dog'),
    path('delete/<int:id>/', delete_dog, name='delete_dog'),
    path('customer', list_customers, name='list_customers'),
    path('new-customer', create_customer, name='create_customer'),
    path('update-customer/<int:id>/', update_customer, name='update_customer'),
]