from django.urls import path

urlpatterns = [
    path('', list_dogs, name='list_dogs'),
    path('new', create_dog, name='create_dog'),
    path('update/<int:id>/', update_dog, name='update_dog'),
    path('delete/<int:id>/', delete_dog, name='delete_dog'),
]