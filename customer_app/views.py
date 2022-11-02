from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'customer_templates/home.html')

def product_details(request):
    return render(request,'customer_templates/product_details.html')

def cart(request):
    return render(request,'customer_templates/cart.html')

def my_orders(request):
    return render(request,'customer_templates/my_orders.html')
    
def password(request):
    return render(request,'customer_templates/change_password.html')

def profile(request):
    return render(request,'customer_templates/profile.html')