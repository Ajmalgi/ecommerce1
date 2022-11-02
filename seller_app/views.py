from django.shortcuts import render

# Create your views here.
def seller_home(request):
    return render(request,'seller_templates/home2.html')

def add_product(request):
    return render(request,'seller_templates/add_product.html')
    
def productcatalog(request):
    return render(request,'seller_templates/product_catalogus.html')
  
def my_orders(request):
    return render(request,'seller_templates/my_orders.html')

 
def update_stock(request):
    return render(request,'seller_templates/update_stock.html')


def change_password(request):
    return render(request,'seller_templates/change_password.html')


def seller_profile(request):
    return render(request,'seller_templates/seller_profile.html')