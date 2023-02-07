from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Products, Country
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from .serializers import CountrySerializer



# Create your views here.
def index(request):
    product = Products.objects.all().values()
    print(product)
    template = loader.get_template('index.html')
    context = {
        'name': 'TEST FROM VIEWS',
        'products': product,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    product = Products.objects.get(id=id)
    context = {
        'products': product
    }
    template = loader.get_template('details.html')
    return HttpResponse(template.render(context,request))

def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Was Created For ' + user)
            return redirect('login')

    context = {
        'form':form
    }
    template = loader.get_template('register.html')
    return render(request, 'register.html', context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username or password inccorect')

    return render(request, 'login.html')

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()