from django.shortcuts import render
from.models import Product,AboutUs,Contacts

# Create your views here.

def homepage(request):
    products = Product.objects.all()
    return render(request,'products/products.html',{"products":products})







def AboutUs_page(request):
    abouts = AboutUs.objects.all()
    return  render(request,'products/aboutus.html',{"about us":abouts})

def Contacts_page(request):
    contacts = Contacts.objects.all()
    return  render(request,'products/contacts.html',{"contacts":contacts})