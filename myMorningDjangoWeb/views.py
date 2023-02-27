from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def product(request):
    return render(request, 'product.html')


# this is a user function
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('my-register')
        else:
            messages.success(request, 'Account creation failed')
            return redirect('my-register')

    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
