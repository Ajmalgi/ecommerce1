from django.shortcuts import render

# Create your views here.
def eadmin(request):
    return render(request,'eadmin_templates/home3.html')

def approve_sellers(request):
    return render(request,'eadmin_templates/approve_sellers.html')

def view_sellers(request):
    return render(request,'eadmin_templates/view_sellers.html')

def view_customers(request):
    return render(request,'eadmin_templates/view_customers.html')

def change_password(request):
    return render(request,'eadmin_templates/change_password.html')