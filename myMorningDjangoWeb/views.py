from django.shortcuts import render
from .forms import UserRegForm


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
    register_button = request.POST.get('m-btn-reg')
    name = ''
    email = ''
    password = ''

    form = UserRegForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
    context = {'form': form, 'name': name, 'email': email,
               'password': password, 'register_button': register_button}
    return render(request, 'register.html', context)
