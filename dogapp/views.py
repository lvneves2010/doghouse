from django.shortcuts import render, redirect
from .models import Dog, Customer

def list_dogs(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs.html', {'dogs': dogs})

def create_dog(request):
    form = DogForm(request.POST or None)

    if form.is_valid()
        form.save()
        return redirect('list_dogs')

    return render(request, 'products-form.html', {'form': form})

def update_dog(request, id):
    dog = Dog.objects.get(id=id)
    form = DogForm(request.POST or None, instance=dog)

    if form.is_valid()
        form.save()
        return redirect('list_dogs')

    return render(request, 'products-form.html', {'form': form})


