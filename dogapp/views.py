from django.shortcuts import render, redirect
from .models import Dog, Customer
from .forms import DogForm, CustomerForm

def list_dogs(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs.html', {'dogs': dogs})

def create_dog(request):
    form = DogForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_dogs')

    return render(request, 'dogs-form.html', {'form': form})

def update_dog(request, id):
    dog = Dog.objects.get(id=id)
    form = DogForm(request.POST or None, instance=dog)

    if form.is_valid():
        form.save()
        return redirect('list_dogs')

    return render(request, 'dogs-form.html', {'form': form, 'dog': dog})

def delete_dog(request, id):
    dog = Dog.objects.get(id=id)

    if request.method == POST:
        dog.delete()
        return redirect('list_dogs')

    return render(request, 'dogs-delete-confirm.html', {'dog': dog})

def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def create_customer(request):
    form = CustomerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_customers')

    return render(request, 'customers-form.html', {'form': form})

def update_customer(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST or None, instance=customer)

    if form.is_valid():
        form.save()
        return redirect('list_customers')

    return render(request, 'customers-form.html', {'form': form, 'customer': customer})

def delete_customer(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == POST:
        customer.delete()
        return redirect('list_customers')

    return render(request, 'customers-delete-confirm.html', {'customer': customer})


